FROM python:3.7


WORKDIR /home/app
ADD /fpl_api ../fpl_api
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN jupyter nbextension enable --py --sys-prefix qgrid

COPY src /home/app/src

CMD [ "python", "./src/main.py" ]