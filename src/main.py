import asyncio
from datetime import datetime
import pickle

import aiohttp
import pandas as pd

from fpl import FPL

from team import Team
from position import Position


async def main():
    date_str = datetime.today().strftime('%Y-%m-%d')
    players_df = await get_players_df(date_str)
    print(players_df)


async def get_players_df(date_str):
    todays_player_pickle = f"""/home/app/data/{date_str}_player_df.pickle"""
    try:
        players_df = pickle.load(open(todays_player_pickle, "rb"))
    except (OSError, IOError) as e:
        players_df = await call_player_api_for_df()
        pickle.dump(players_df, open(todays_player_pickle, "wb"))
    return players_df


async def call_player_api_for_df():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players(include_summary=True, return_json=True)
    players_df = pd.DataFrame(players)
    players_df["name"] = players_df["first_name"] + " " + players_df["second_name"]
    players_df["team_name"] = players_df["team"].apply(lambda x: Team(x).name)
    players_df["position"] = players_df["element_type"].apply(lambda x: Position(x).name)
    players_df.set_index("id", inplace=True)
    return players_df


if __name__ == "__main__":
    asyncio.run(main())