from src.db.mongo import Mongo


class Payment:

    def __init__(self):
        self.__payment_id = None
        self.__description = None
        self.__image_url = None

    def with_payment_id(self, payment_id: str):
        self.__payment_id = payment_id
        return self

    def with_image_url(self, image_url: str):
        self.__image_url = image_url
        return self

    def with_description(self, description: str):
        self.__description = description
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
            '_id': self.__payment_id,
            'description': self.__description,
            'image_url': self.__image_url
        }

    @classmethod
    def __from_db_document(cls, document):
        return Payment()\
            .with_payment_id(document['_id'])\
            .with_description(document['description'])\
            .with_image_url(document['image_url'])

    @classmethod
    def __collection(cls):
        return Mongo().get().db.payments

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key.replace('_Payment__', ''), value)
