from src.db.mongo import Mongo


class Category:

    def __init__(self):
        self.__name = None

    def with_name(self, name: str):
        self.__name = name
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
        return {'_id': self.__name}

    @classmethod
    def __from_db_document(cls, document):
        return Category().with_name(document['_id'])

    @classmethod
    def __collection(cls):
        return Mongo().get().db.categories

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key.replace('_Category__', ''), value)
