FROM python:3.8.1-slim-buster 

WORKDIR /app
COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

CMD flask run --host=0.0.0.0
