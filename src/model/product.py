from src.db.mongo import Mongo


class Product:
    """ Abstract (or not) class to represent all menu products. """

    def __init__(self):
        self.__product_id = None
        self.__price = float(0)
        self.__description = None
        self.__category = None
        self.__in_store = 0
        self.__veggie_apt = False
        self.__celiac_apt = False
        self.__image_url = None

    def with_id(self, product_id: str):
        self.__product_id = product_id
        return self

    def with_price(self, price: float):
        self.__price = price
        return self

    def with_description(self, description: str):
        self.__description = description
        return self

    def with_category(self, category: str):
        self.__category = category
        return self

    def with_items_in_store(self, in_store: int):
        self.__in_store = in_store
        return self

    def is_veggie_apt(self, value: bool):
        self.__veggie_apt = value
        return self

    def is_celiac_apt(self, value: bool):
        self.__celiac_apt = value
        return self

    def with_image_url(self, image_url: str):
        self.__image_url = image_url
        return self

    def store(self):
        self.__collection().insert(self.__to_db_document())
        return self

    def update(self):
        document = self.__to_db_document()
        query = {'_id': document.pop('_id')}
        self.__collection().find_one_and_update(filter=query, update={'$set': document})
        return self

    @classmethod
    def remove(cls, product_id):
        cls.__collection().find_one_and_delete({'_id': product_id})

    @classmethod
    def find(cls, product_id):
        document = cls.__collection().find_one({'_id': product_id})
        return None if not document else cls.__from_db_document(document)

    @classmethod
    def find_all(cls):
        return [cls.__from_db_document(document) for document in cls.__collection().find({})]

    def __to_db_document(self):
        return {
            '_id': self.__product_id,
            'description': self.__description,
            'price': self.__price,
            'category': self.__category,
            'in_store': self.__in_store,
            'veggie_apt': self.__veggie_apt,
            'celiac_apt': self.__celiac_apt,
            'image_url': self.__image_url
        }

    @classmethod
    def __from_db_document(cls, document):
        return Product() \
            .with_id(document['_id']) \
            .with_description(document['description']) \
            .with_price(document['price']) \
            .with_category(document['category']) \
            .with_items_in_store(document['in_store']) \
            .is_veggie_apt(document['veggie_apt']) \
            .is_celiac_apt(document['celiac_apt']) \
            .with_image_url(document['image_url'])

    @classmethod
    def __collection(cls):
        return Mongo().get().db.products

    def __str__(self):
        return str({k.replace('_Product__', ''): v for k, v in self.__dict__.items()})

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key.replace('_Product__', ''), value)
