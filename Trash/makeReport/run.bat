@echo off

echo Activating venv...

call venv/Scripts/activate.bat

echo Run merger...

py main.py

echo Your report is ready!