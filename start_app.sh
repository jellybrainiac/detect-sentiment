#!/bin/sh

cd ./src
# Assuming uvicorn requires typing_extensions (modify if not)
if [ -n "$VIRTUAL_ENV" ]; then
  # Use uvicorn within virtual environment (if activated)
  uvicorn app:app --host=0.0.0.0 --port=8080 --reload
else
  # Use uvicorn outside virtual environment
  python3 -m uvicorn app:app --host=0.0.0.0 --port=8080 --reload
fi

