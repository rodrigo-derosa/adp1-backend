from flask import request
from flask_restful import Resource

from src.model.promotion import Promotion


class PromotionResource(Resource):

    @staticmethod
    def get():
        return [dict(promotion) for promotion in Promotion.find_all()]

    @staticmethod
    def post():
        Promotion()\
            .with_promotion_id(request.json.get('promotion_id'))\
            .with_products(request.json.get('products'))\
            .with_price(request.json.get('price'))\
            .store()

    @staticmethod
    def delete(promotion_id):
        Promotion.remove(promotion_id)
