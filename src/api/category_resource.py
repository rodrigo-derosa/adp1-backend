from flask import request
from flask_restful import Resource

from src.model.category import Category


class CategoryResource(Resource):

    @staticmethod
    def get():
        return [dict(category) for category in Category.find_all()]

    @staticmethod
    def post():
        Category()\
            .with_name(request.json.get('name'))\
            .store()

    @staticmethod
    def delete(category_name):
        Category.remove(category_name)
