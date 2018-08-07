
from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask_restful import fields, marshal_with
import datetime

from Model.Retail import SingleTransaction
from Resources.Transaction import *

app = Flask(__name__)
api = Api(app)

##################

api.add_resource(TransactionList, '/transactions')
api.add_resource(Transaction, '/transaction/<transaction_id>')


if __name__ == '__main__':
    app.run(debug=False, port=5003)





