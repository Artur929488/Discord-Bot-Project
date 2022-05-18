@echo off 

call %~dp0venv\Scripts\activate

cd %~dp0bot

set TOKEN=Ваш токен

python main.py

pause
