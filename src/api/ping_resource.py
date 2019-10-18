from flask_restful import Resource


class PingResource(Resource):

    @staticmethod
    def get():
        return "OK"
