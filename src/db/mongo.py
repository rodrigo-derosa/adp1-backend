from flask_pymongo import PyMongo

from src.utils.singleton import Singleton


class Mongo(metaclass=Singleton):

    def __init__(self):
        self.__db = PyMongo()

    def get(self):
        return self.__db
