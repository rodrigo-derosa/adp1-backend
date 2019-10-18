from flask import request
from flask_restful import Resource

from src.model.payment import Payment


class PaymentResource(Resource):

    @staticmethod
    def get():
        return [dict(payment) for payment in Payment.find_all()]

    @staticmethod
    def post():
        Payment()\
            .with_payment_id(request.json.get('payment_id'))\
            .with_description(request.json.get('description'))\
            .with_image_url(request.json.get('image_url'))\
            .store()

    @staticmethod
    def delete(payment_id):
        Payment.remove(payment_id)
