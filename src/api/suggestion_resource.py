from flask import request
from flask_restful import Resource

from src.model.suggestion import Suggestion


class SuggestionResource(Resource):

    @staticmethod
    def get():
        return [dict(suggestion) for suggestion in Suggestion.find_all()]

    @staticmethod
    def post():
        Suggestion()\
            .with_suggestion_id(request.json.get('suggestion_id'))\
            .with_message(request.json.get('message'))\
            .store()

    @staticmethod
    def delete(suggestion_id):
        Suggestion.remove(suggestion_id)
