from flask import Flask, request
from flask_cors import CORS, cross_origin
from service import autocomplete_from_docs, autocomplete_with_gpt, explanation_with_gpt

app = Flask(__name__)
CORS(app, support_credentials=True)


@app.route("/autocomplete", methods=['GET'])
def get_autocompletion_from_docs():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    query = request.args['query']
    suggestions = autocomplete_from_docs(query)

    # Complement with GPT's suggestions if there are less than 3 suggestions
    if len(suggestions) < 3:
        suggestions = autocomplete_with_gpt(query) + suggestions

    return suggestions


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
    app.run(host='0.0.0.0', port=8000, debug=True)