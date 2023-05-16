# DIP_programming

# Command:
<!-- Create a virtual environment in the terminal -->
py -m venv .venv

<!-- Upgrade pip: -->
py -m pip install --upgrade pip

<!-- Set-Execution Policy to allow the current user to execute scripts as follows -->
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope CurrentUser

<!-- Install packages -->
pip install -r .\requirements.txt

<!-- Freeze packages -->
python -m pip freeze > requirements.txt

# Some problems:
Transfer variable from a frame to another frame. 
Solution: init them with updated grandparent before deploying.

