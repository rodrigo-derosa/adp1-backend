from flask import Flask
from flask_cors import CORS
from flask_restful import Api

from src.db.mongo import Mongo


class FlaskApp:

    def __init__(self, name):
        self.app = Flask(name)

    def with_mongo_db(self, db_name):
        self.app.config['MONGO_DBNAME'] = db_name
        self.app.config['MONGO_URI'] = f'mongodb://localhost:27017/{db_name}'
        Mongo().get().init_app(self.app)
        return self

    def with_cors(self):
        CORS(self.app)
        return self

    def with_endpoints(self, endpoints):
        api = Api(self.app)
        for handler, paths in endpoints:
            api.add_resource(handler, *paths)
        return self

    def start(self, port=8080):
        self.app.run(port=port, threaded=True)
