
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_restful import fields, marshal_with
import datetime

from Model.Retail import SingleTransaction
from Resources.Transaction import *

app = Flask(__name__)
api = Api(app)


SingleTransaction1 = SingleTransaction('1',34.5, 'Yossi', datetime.date(2013, 11, 12))
SingleTransaction2 = SingleTransaction('2',34.5, 'Yossi', datetime.date(2014, 11, 12))
SingleTransaction3 = SingleTransaction('3',34.5, 'Yossi', datetime.date(2015, 11, 12))
SingleTransaction4 = SingleTransaction('4',34.5, 'Yossi', datetime.date(2016, 11, 12))


TRANSACTIONS = {
    'transaction1': SingleTransaction1,
    'transaction2': SingleTransaction2,
    'transaction3': SingleTransaction3,
}


def abort_if_todo_doesnt_exist(transaction_id):
    if transaction_id not in TRANSACTIONS:
        abort(404, message="transaction {} doesn't exist".format(transaction_id))



class Transaction(Resource):

    @marshal_with(transaction_fields)
    def get(self, transaction_id):
        abort_if_todo_doesnt_exist(transaction_id)
        return TRANSACTIONS[transaction_id]

    @marshal_with(transaction_fields)
    def delete(self, transaction_id):
        abort_if_todo_doesnt_exist(transaction_id)
        del TRANSACTIONS[transaction_id]
        return 'deleted', 204

    @marshal_with(transaction_fields)
    def put(self, transaction_id):
        args = transaction_parser.parse_args()
        transaction = {'customerName': args['customerName']}
        TRANSACTIONS[transaction_id] = task
        return transaction, 201


class TransactionList(Resource):

    @marshal_with(transaction_fields)
    def get(self):
        return TRANSACTIONS
       
    @marshal_with(transaction_fields)
    def post(self):
        args = transaction_parser.parse_args()
        transaction_id = int(max(TRANSACTIONS.keys()).lstrip('transaction')) + 1
        transaction_id = 'transaction%i' % transaction_id
        TRANSACTIONS[transaction_id] = {'customerName': args['customerName']}
        return True,201


##################
api.add_resource(TransactionList, '/transactions')
api.add_resource(Transaction, '/transaction/<transaction_id>')


if __name__ == '__main__':
    app.run(debug=True,port=5001)





