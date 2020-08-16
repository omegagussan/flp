from enum import Enum, unique

@unique
class Position(Enum):
    GK = 1
    DEF = 2
    MID = 3
    FWD = 4