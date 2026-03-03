#!/bin/bash

# Run FastAPI backend
echo "Starting Portfolio Backend (FastAPI)..."
uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

