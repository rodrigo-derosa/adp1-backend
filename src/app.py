from src.api.api_utils import api_endpoints
from src.utils.flask_app import FlaskApp

if __name__ == '__main__':
    FlaskApp(__name__)\
        .with_cors()\
        .with_endpoints(api_endpoints())\
        .with_mongo_db(db_name='virtual_menu')\
        .start()
