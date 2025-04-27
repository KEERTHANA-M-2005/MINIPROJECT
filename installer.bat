@echo off
:: Create a virtual environment if it doesn't exist
if not exist "venv" (
    python -m venv venv
)

:: Activate the virtual environment
call venv\Scripts\activate

:: Install dependencies from requirements.txt
pip install -r requirements.txt

:: Keep the terminal open after executing
pause
