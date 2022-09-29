#! /usr/bin/env sh
# Start Gunicorn
exec gunicorn -k uvicorn.workers.UvicornWorker --bind "0.0.0.0:8080" --workers 4  --timeout 120 main:app