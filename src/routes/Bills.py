from flask import Blueprint, jsonify

# Models
from models.BillsModel import BillModel

main = Blueprint('bills_blueprint', __name__)


@main.route('/')
def get_bills():
    try:
        bills = BillModel.get_bill()
        print("retorno", bills)
        return jsonify(bills)
    except Exception as ex:
        return jsonify({'message': str(ex)}), 500
