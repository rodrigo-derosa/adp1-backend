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
            .with_description(request.json.get('description'))\
            .with_price(request.json.get('price'))\
            .store()

    @staticmethod
    def patch(promotion_id):
        body = request.json
        promotion = Promotion.find(promotion_id)
        if body.get('price'): promotion.with_price(body.get('price'))
        if body.get('description'): promotion.with_description(body.get('description'))
        promotion.update()

    @staticmethod
    def delete(promotion_id):
        Promotion.remove(promotion_id)
