from flask import Flask, request
from flask_cors import CORS, cross_origin
import service 
import mock_service
from config import fake_service

app = Flask(__name__)
CORS(app, support_credentials=True)

@cross_origin(supports_credentials=True)
@app.route("/autocomplete", methods=['GET'])
def get_autocompletion_from_docs():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    if fake_service:
        return mock_service.autocomplete_from_docs()

    query = request.args['query']
    suggestions = service.autocomplete_from_docs(query)

    # Complement with GPT's suggestions if there are less than 3 suggestions
    if len(suggestions) < 3:
        suggestions = service.autocomplete_with_gpt(query) + suggestions

    return suggestions

@cross_origin(supports_credentials=True)
@app.route("/autocomplete/gpt", methods=['GET'])
def get_autocompletion_with_gpt():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    if fake_service:
        return mock_service.autocomplete_with_gpt()

    query = request.args['query']

    return service.autocomplete_with_gpt(query)

@cross_origin(supports_credentials=True)
@app.route("/autocomplete/gpt/analysis", methods=['GET'])
def get_explanation_with_gpt():
    if ('query' not in request.args):
        return "Error: No query field provided. Please specify a query."

    if fake_service:
        return mock_service.explanation_with_gpt()

    query = request.args['query']

    return service.explanation_with_gpt(query)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)