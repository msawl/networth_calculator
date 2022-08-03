from crypt import methods
from nturl2path import url2pathname
from re import T
from flask import Blueprint, jsonify, request
from data_models.transactions import Transactions
from lib.exchange_rates import convert_currency


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


@transactinons_endpoints.route("exchangerate", methods=["GET"])
def get_exchangerate():

    response = convert_currency(currency_from="USD", currency_to="EUR", amount=1)

    rate = response["rates"]

    return {"rate": rate}


@transactinons_endpoints.route("exchangerate/<currency>", methods=["GET"])
def get_exchangerate_for_currency(currency):

    response = convert_currency(currency_from="USD", currency_to="EUR", amount=1)

    rate = response["rates"][currency]

    return {"rate": rate}
