FROM python:3.11-slim-bookworm

# variables
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# setting work directory
WORKDIR usr/src/app

# install psycopg dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# install dependencies
RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip install -r requirements.txt


COPY . .

# EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
