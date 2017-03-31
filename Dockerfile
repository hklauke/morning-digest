FROM python:3

RUN mkdir /script
ADD . /script/
WORKDIR /script/

RUN echo "deb http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list
RUN wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add -

RUN apt-get update
RUN apt-get install xvfb -y
RUN apt-get install sendmail -y
RUN apt-get install google-chrome-stable -y
RUN pip install -r requirements.txt

CMD [ "python", "morning_digest.py"]
