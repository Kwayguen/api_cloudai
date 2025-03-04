
FROM continuumio/miniconda3

WORKDIR /home/app/

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY main.py .

CMD uvicorn main:app --port $PORT --host 0.0.0.0



