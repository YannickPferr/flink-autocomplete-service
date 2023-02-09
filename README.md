# flink-autocomplete-service

## Use cases

1. Create suggestions based on incomplete queries

get /autocomplete?query="sele"
response: []{
{statement: "select _ from orders", description: "selects all data from table orders"},
{statement: "select _ from orders", description: "selects all data from table orders"}
}

get /autocomplete/gpt?query="sele"
response: []{
{statement: "select _ from orders", description: "selects all data from table orders"},
{statement: "select _ from orders", description: "selects all data from table orders"}
}

get /autocomplemente/gpt/analysis?query="select \* from orders"
response: string
" This query fetchs the database...."

## Installation

```
# clone the repo
git clone https://github.com/YannickPferr/flink-autocomplete-service.git
cd flink-autocomplete-service
# activate virtual env
python -m venv venv
source venv/bin/activate
# install packages
pip install -r requirements.txt
cd frontend 
npm install
```

## Usage

```
# start the server
python backend/server.py

# start the frontend
cd frontend
npm start
```
