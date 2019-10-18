from flask import request
from flask_restful import Resource

from src.model.product import Product


class ProductResource(Resource):

    @staticmethod
    def post():
        Product()\
            .with_id(request.json.get('product_id', None))\
            .with_price(request.json.get('price', float(0)))\
            .with_description(request.json.get('description'))\
            .with_category(request.json.get('category'))\
            .with_items_in_store(request.json.get('in_store', 0))\
            .is_veggie_apt(request.json.get('veggie_apt', False))\
            .is_celiac_apt(request.json.get('celiac_apt', False))\
            .with_image_url(request.json.get('image_url'))\
            .store()

    @staticmethod
    def patch(product_id):
        body = request.json
        product = Product.find(product_id)
        if body.get('price'): product.with_price(body.get('price'))
        if body.get('description'): product.with_description(body.get('description'))
        if body.get('category'): product.with_category(body.get('category'))
        if body.get('in_store'): product.with_items_in_store(body.get('in_store'))
        if body.get('veggie_apt'): product.is_veggie_apt(body.get('veggie_apt'))
        if body.get('celiac_apt'): product.is_celiac_apt(body.get('celiac_apt'))
        if body.get('image_url'): product.with_image_url(body.get('image_url'))
        product.update()

    @staticmethod
    def get(product_id=None):
        if not product_id:
            return [dict(product) for product in Product.find_all()]
        return dict(Product.find(product_id))

    @staticmethod
    def delete(product_id):
        Product.remove(product_id)
