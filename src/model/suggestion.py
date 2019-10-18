from src.db.mongo import Mongo


class Suggestion:

    def __init__(self):
        self.__suggestion_id = None
        self.__message = None

    def with_suggestion_id(self, suggestion_id: str):
        self.__suggestion_id = suggestion_id
        return self

    def with_message(self, message: str):
        self.__message = message
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
            '_id': self.__suggestion_id,
            'message': self.__message
        }

    @classmethod
    def __from_db_document(cls, document):
        return Suggestion()\
            .with_suggestion_id(document.get('_id'))\
            .with_message(document.get('message'))

    @classmethod
    def __collection(cls):
        return Mongo().get().db.suggestions

    def __iter__(self):
        for key, value in self.__dict__.items():
            yield (key.replace('_Suggestion__', ''), value)
