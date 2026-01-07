# Dockerfile for Puddle Django Application

# Use official Python 3.12 slim image as base image
FROM python:3.12-slim 

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory in the container to /app
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Command to run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
