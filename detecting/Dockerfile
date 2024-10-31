FROM python:3.10-slim AS builder

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -U pip && \
    pip install --no-cache-dir -r requirements.txt --extra-index-url https://download.pytorch.org/whl/cu118

COPY . /app/

# Build stage for runtime image
FROM scratch

WORKDIR /app

# Install dependencies from the builder stage
COPY --from=builder /app/ /app/

# Install system dependencies
RUN apt-get update && \
    apt-get install -y ffmpeg libsm6 libxext6 && \
    rm -rf /var/lib/apt/lists/*
