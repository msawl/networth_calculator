import pytest
from api import api


def test_transactions_get():
    actual = api.test_client().get("/my_business/transactions")
    assert actual.status_code == 200


def test_currency_1():
    actual = api.test_client().get("/my_business/exchangerate/CAD")
    print(actual.text)
    assert actual.status_code == 200


def test_currency_2():
    actual = api.test_client().get("/my_business/exchangerate/ABC")
    print(actual.text)
    assert actual.status_code == 404


def test_networth():
    actual = api.test_client().get("/my_business/transactions/networth")
    print(actual.text)
    actual_text = actual.text

    errors = []

    for i in ["liabilities", "assets", "networth"]:
        if i not in actual_text:
            errors.append(i)

    assert not errors, f"errors occured at: {errors}"
