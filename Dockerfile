FROM python:3.7

ADD . /haiku_scrapper

WORKDIR /haiku_scrapper

RUN pip3 install -r requirements.txt

CMD ["python", "haiku_scrapper", "-path", "data"]