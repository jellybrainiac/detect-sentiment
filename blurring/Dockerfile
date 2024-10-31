# FROM python:3.10-slim
FROM ultralytics/ultralytics:latest

WORKDIR /app

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Install the application dependencies
COPY requirements.txt /app/
# RUN pip install -U pip && \
#     pip install torch==2.5.0 torchvision==0.20.0

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . /app/
