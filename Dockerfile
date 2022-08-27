# Dockerfile, Image, Container
FROM python:3.10.6

ADD Movie_selector.py .

RUN pip install beautifulsoup4 requests

CMD [ "python", "./Movie_selector.py" ]