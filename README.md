# Getting Started

## requirements

* python3

### Clone the repository, Make virtual environment and install dependencies

* Windows
```
# clone the repository
git clone https://github.com/triaton/fastapi-email-sender.git

cd fastapi-email-sender

# make virtual environemnt
py -m venv env

# activate the virtual environment
.\env\Scripts\activate.bat

# install dependencies
py -m pip install -r requirements.txt

# start the server for development
uvicorn main:app --reload

# start the server for production
uvicorn main:app --port 80 --host 0.0.0.0
```

* Linux
```
# clone the repository
git clone https://github.com/triaton/fastapi-email-sender.git

cd fastapi-email-sender

# make virtual environemnt
virtuanenv env

# activate the virtual environment
source ./env/Scripts/activate

# install dependencies
pip install -r requirements.txt

# start the server for development
uvicorn main:app --reload

# start the server for production
uvicorn main:app --port 80 --host 0.0.0.0
```
