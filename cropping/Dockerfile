FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && \ 
    apt-get install ffmpeg libsm6 libxext6  -y && \
    rm -rf /var/lib/apt/lists/*

# Install the application dependencies
COPY requirements.txt /app/
RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu118

# Copy in the source code
COPY . /app/
