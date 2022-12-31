Install Python

Install Python (version 3.10).

Main frameworks and packages:

FastAPI
SQLAlchemy


Set and activate virtual environment
In project folder, execute the following commands:

pip install pipenv
export PIPENV_VENV_IN_PROJECT="enabled"
mkdir .venv
pipenv shell
source .venv/Scripts/activate



Install dependencies on virtual env
In project folder, execute the following command:

pipenv install --dev



Set environment variables
In project folder, create a .env file from .env.example

cp .env.example .env


Set proper values for the environment variables on .env

Run

python main.py