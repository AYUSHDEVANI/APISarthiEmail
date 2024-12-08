# Use the official Python image
FROM python:3.13-slim

# Set the working directory in the container
WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libcairo2 \
    libpango1.0-0 \
    libpangocairo-1.0-0 \
    libpangoft2-1.0-0 \
    libgdk-pixbuf2.0-0 \
    libffi-dev \
    shared-mime-info \
    && apt-get clean

# Copy requirements file to the container
COPY requirements.txt requirements.txt

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container
COPY . .

# Expose the port the app runs on
EXPOSE 5000

# Set environment variable to avoid Python buffering issues
ENV PYTHONUNBUFFERED=1

# Command to run the application
# CMD ["python", "api.py"]
CMD ["gunicorn", "-w", "4", "api:app", "-b", "0.0.0.0:5000"]
