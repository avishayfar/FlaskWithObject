
from Model.Retail import SingleTransaction
from flask_restful import fields, marshal_with, reqparse, Resource
import datetime


SingleTransaction1 = SingleTransaction(['physics', 'chemistry', '1997', '2000'])
SingleTransaction2 = SingleTransaction(['physics', 'chemistry', '1997', '2000'])
SingleTransaction3 = SingleTransaction(['physics', 'chemistry', '1997', '2000'])
SingleTransaction4 = SingleTransaction(['physics', 'chemistry', '1997', '2000'])


TRANSACTIONS = {
    'transaction1': SingleTransaction1,
    'transaction2': SingleTransaction2,
    'transaction3': SingleTransaction3,
}

transaction_parser = reqparse.RequestParser()  
transaction_parser.add_argument('parameterLst', required=True ,help='The id of the transaction', action='append')


transaction_fields = {
    'parameterLst': fields.List(fields.String),
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
        return TRANSACTIONS['transaction1']  #TRANSACTIONS
       
    @marshal_with(transaction_fields)
    def post(self):
        args = transaction_parser.parse_args()
        parameterLst = args['parameterLst']
        transaction_id = int(max(TRANSACTIONS.keys()).lstrip('transaction')) + 1
        transaction_id = 'transaction%i' % transaction_id

        st = SingleTransaction(parameterLst)
        TRANSACTIONS[transaction_id] = st
        return TRANSACTIONS[transaction_id] 
        #return True,203


