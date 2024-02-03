## datafun-05-sql

## Clone repository
clone repo in VS Code

## New items
create .venv, .gitignore, requirements.txt


## Activate Virtual Environment
python -m venv .venv
.\.venv\Scripts\Activate


## Add to gitignore
.venv
.vscode


## Install and Freeze Dependencies
Open requirements file and add packages
pandas
pyarrow

# Run install
py -m pip install -r requirements.txt

# Freeze dependencies
py -m pip freeze > requirements.txt


## Git Add and Commit
git add .
git commit -m "initial commit"

# Push to GitHub
git push origin main


