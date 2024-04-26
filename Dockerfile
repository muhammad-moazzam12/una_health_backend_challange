FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

RUN apt-get update && apt-get install -y \
    libssl-dev \
    libffi-dev \
    libpq-dev \
    build-essential \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

COPY ./una_health /app/
COPY ./requirements.txt /app/

RUN pip install --upgrade pip \
    && pip install -r requirements.txt

EXPOSE 8000


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
