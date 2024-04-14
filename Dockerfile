FROM python:3.8-alpine

WORKDIR /app

COPY one.py ./
COPY requirements.txt ./

RUN pip install --upgrade pip && pip install -r requirements.txt

CMD ["python", "one.py"]