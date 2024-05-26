@echo off
call .\venv\Scripts\activate
uvicorn app.main:app --reload --host="192.168.1.8" --port="8000"
pause
