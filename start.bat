@echo off 

call %~dp0venv\Scripts\activate

cd %~dp0bot

set TOKEN=ODMxODAzMTE2MDcxOTQ0MjEy.YHajBQ.nQEishYYihfRVj9zrDFDItulmBo

python main.py

pause