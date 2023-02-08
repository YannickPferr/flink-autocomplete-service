from flask import Flask, request

from openapi import generateGPTAutocompletions
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/autocomplete/gpt", methods=['GET'])
def getAutocompleteGPT():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    query = request.args['query']

    return generateGPTAutocompletions(query)


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
