from Model.Retail import SingleTransaction
from flask_restful import fields, marshal_with, reqparse, Resource
import datetime

transaction_parser = reqparse.RequestParser()  
transaction_parser.add_argument('id', required=True ,help='The id of the transaction')
transaction_parser.add_argument('balancedue'  , type=int , required=True)
transaction_parser.add_argument('customerName', required=True)
#parser.add_argument('startTime'   , type=datetime.date , required=False)


transaction_fields = {
    'id': fields.String,
    'customerName': fields.String,
    'balancedue': fields.Integer,
    #'startTime': fields.DateTime,
}


