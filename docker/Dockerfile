FROM python:3.10

WORKDIR /app

COPY backend/ /app/backend/
COPY backend/requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "backend/app.py"]