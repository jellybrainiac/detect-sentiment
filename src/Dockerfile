FROM python:3.10-slim
RUN echo `Creating WORKDIR`
WORKDIR /detect

COPY . /detect/

RUN pip3 install -U pip
RUN pip3 install -r requirements.txt --no-cache-dir
RUN echo `Done Setting ${WORKDIR}`
RUN ls -la
CMD ["python3 -m" , "uvicorn", "app:app", "--host=0.0.0.0", "--port=8080", "--reload"]