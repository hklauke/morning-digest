FROM python:3

RUN mkdir /script
COPY ./chromedriver /usr/bin/chromedriver
ADD . /script/
WORKDIR /script/

RUN pip install -r requirements.txt
RUN apt-get install sendmail
RUN apt-get install

CMD [ "python", "morning_digest.py"]
