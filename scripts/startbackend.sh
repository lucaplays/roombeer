#!/bin/bash
cd ..
python -m venv venv_backend
source venv_backend/bin/activate
pip install "fastapi[standard]"
fastapi run main.py
