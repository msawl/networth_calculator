from crypt import methods
from nturl2path import url2pathname
from re import S, T
from flask import Blueprint, jsonify, request, make_response
from data_models.transactions import Transactions
from lib.exchange_rates import convert_currency
from datetime import datetime, timedelta
from lib.errors import SymbolNotFound


transactinons_endpoints = Blueprint(
    name="my_business", url_prefix="/my_business/", import_name=__name__
)


@transactinons_endpoints.route("transactions", methods=["GET"])
def get_transactinons():
    all_transactions = Transactions.get_transactions_by_type()
    print(all_transactions)

    response = {"results": all_transactions}
    return response


@transactinons_endpoints.route("transactions", methods=["POST"])
def post_transactinons():
    pass


@transactinons_endpoints.route("transactions/<transaction_id>", methods=["PATCH"])
def edit_transactinon(transaction_id):
    transaction = Transactions.get_transaction(transaction_id)

    request_params = request.get_json()

    if request_params.get("amount"):
        transaction.amount = request_params["amount"]

    transaction.save_to_db()

    return transaction.json()


@transactinons_endpoints.route("transactions/networth", methods=["GET"])
def get_networth():
    all_transactions = Transactions.get_transactions_by_type()

    assets = 0
    liabilities = 0
    for i in all_transactions["assets"]:
        assets += i["amount"]

    for j in all_transactions["liabilities"]:
        liabilities += j["amount"]

    networth = assets - liabilities

    return {"networth": networth, "assets": assets, "liabilities": liabilities}


@transactinons_endpoints.route("exchangerate/<currency>", methods=["GET"])
def get_exchangerate_for_currency(currency):

    response = convert_currency()

    try:
        rate = response["rates"][currency]
    except Exception as e:
        raise SymbolNotFound(
            f"The currrency symbol {currency} is not found in database or does not exist"
        )

    output = make_response({"rate": rate})
    output.cache_control.max_age = 600
    output.cache_control.must_revalidate = True

    return output
