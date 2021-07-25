FROM python:3.9-alpine

WORKDIR /work

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY api api

CMD ["flask", "run", "--host=0.0.0.0"]