FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cpu

COPY . .

# Build stage for runtime image
FROM python:3.10-slim

WORKDIR /app

# Install dependencies from the builder stage
COPY --from=builder /app/ .

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 && \
    rm -rf /var/lib/apt/lists/*
