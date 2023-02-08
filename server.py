from flask import Flask, request

from openapi import GPTAutocompletions, GPTStatementAnalysis
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/autocomplete/gpt", methods=['GET'])
def getAutocompleteGPT():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    query = request.args['query']

    return GPTAutocompletions(query)


@app.route("/autocomplete/gpt/analysis", methods=['GET'])
def getAnalysisGPT():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    query = request.args['query']

    return GPTStatementAnalysis(query)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
