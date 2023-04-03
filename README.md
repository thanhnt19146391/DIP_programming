# DIP_programming


Command:
Create a virtual environment in the terminal
py -m venv .venv

Upgrade pip:
Set-Execution Policy to allow the current user to execute scripts as follows
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

py -m pip install --upgrade pip

Install packages
pip install -r .\requirements.txt

Set-Execution Policy to allow the current user to execute scripts as follows
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

Freeze packages
python -m pip freeze > requirements.txt 