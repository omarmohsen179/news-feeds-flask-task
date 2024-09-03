
FROM mysql:8.0
COPY schema.sql /docker-entrypoint-initdb.d/
# Use the official Python image.
FROM python:3.10-slim

# Set the working directory.
WORKDIR /usr/src/app

# Install system dependencies.
RUN apt-get update && apt-get install -y default-libmysqlclient-dev gcc

# Install Python dependencies.
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application files.
COPY . .

# Set environment variables.
ENV FLASK_APP=run.py
ENV FLASK_RUN_HOST=0.0.0.0

# Run the application.
CMD ["flask", "run"]
