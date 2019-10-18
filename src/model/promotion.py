from src.db.mongo import Mongo


class Promotion:

    def __init__(self):
        self.__promotion_id = None
        self.__products = None
        self.__price = None

    def with_promotion_id(self, promotion_id: str):
        self.__promotion_id = promotion_id
        return self

    def with_products(self, products: list):
        self.__products = products
        return self

    def with_price(self, price: float):
        self.__price = price
        return self

    def store(self):
        self.__collection().insert(self.__to_db_document())
        return self

    @classmethod
    def find_all(cls):
        return [cls.__from_db_document(document) for document in cls.__collection().find({})]

    @classmethod
    def remove(cls, category_name):
        cls.__collection().find_one_and_delete({'_id': category_name})

    def __to_db_document(self):
        return {
            '_id': self.__promotion_id,
            'products': self.__products,
            'price': self.__price
        }

    @classmethod
    def __from_db_document(cls, document):
        return Promotion()\
            .with_promotion_id(document.get('_id'))\
            .with_products(document.get('products'))\
            .with_price(document.get('price'))

    @classmethod
    def __collection(cls):
        return Mongo().get().db.promotions

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key.replace('_Promotion__', ''), value)
