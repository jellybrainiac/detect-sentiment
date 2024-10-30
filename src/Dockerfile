FROM python:3.10-slim
# FROM ultralytics/ultralytics:latest

WORKDIR /app


RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# Install the application dependencies
COPY requirements.txt ./
RUN pip install -U pip
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118 
# https://github.com/pytorch/pytorch/issues/97580
RUN pip install --no-cache-dir -r requirements.txt

# Copy in the source code
COPY . /app/

# # Setup an app user so the container doesn't run as the root user
# RUN useradd app
# USER app

# CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8080", "--reload"]
