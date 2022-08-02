from flask import Flask
from flask_cors import CORS
from db import db
from data_models.transactions import initialize_db_with_prefilled_data
from resources.transactions import transactinons_endpoints

api = Flask(__name__)
api.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
api.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

api.register_blueprint(transactinons_endpoints)

CORS(api)


@api.before_first_request
def create_tables():
    db.create_all()
    initialize_db_with_prefilled_data()


@api.route("/hello", methods=["GET"])
def hello():
    return {"hello": "I am working!"}


if __name__ == "__main__":
    db.init_app(api)
    api.run(host="127.0.0.1", port=8080, debug=True)
