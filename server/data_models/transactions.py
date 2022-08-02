from db import db
from sample_transactions import sample_transactions


class Transactions(db.Model):
    __tablename__ = "assets"

    id = db.Column(db.Integer, primary_key=True)
    name_of_holding = db.Column(db.String)
    type = db.Column(db.String)
    sub_type = db.Column(db.String)
    amount = db.Column(db.Integer)

    def __init__(self, name_of_holding, type, sub_type, amount):
        self.name_of_holding = name_of_holding
        self.type = type
        self.sub_type = sub_type
        self.amount = amount

    def json(self):
        response = {
            "id": self.id,
            "name_of_holding": self.name_of_holding,
            "type": self.type,
            "sub_type": self.sub_type,
            "amount": self.amount,
        }
        return response

    @classmethod
    def get_all_transactions(cls):
        output = cls.query.all()
        results = []
        for i in output:
            results.append(i.json())
        return results

    @classmethod
    def get_transactions_by_type(cls):
        output = cls.query.all()
        assets = []
        liablities = []

        for i in output:
            out_json = i.json()
            if out_json["type"] == "asset":
                assets.append(out_json)
            else:
                liablities.append(out_json)
        return {"assets": assets, "liabilities": liablities}

    @classmethod
    def get_transaction(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


def initialize_db_with_prefilled_data():
    for transaction in sample_transactions:
        tr = Transactions(
            name_of_holding=transaction["name_of_holding"],
            type=transaction["type"],
            sub_type=transaction["sub_type"],
            amount=transaction["amount"],
        )

        tr.save_to_db()
