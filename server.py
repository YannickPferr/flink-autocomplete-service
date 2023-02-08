from flask import Flask, request
from service import autocomplete_with_docs, autocomplete_with_gpt, explanation_with_gpt

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/autocomplete", methods=['GET'])
def get_autocompletion_with_docs():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    query = request.args['query']

    return autocomplete_with_docs(query)

@app.route("/autocomplete/gpt", methods=['GET'])
def get_autocompletion_with_gpt():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    query = request.args['query']

    return autocomplete_with_gpt(query)

@app.route("/autocomplete/gpt/analysis", methods=['GET'])
def get_explanation_with_gpt():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    query = request.args['query']

    return explanation_with_gpt(query)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
