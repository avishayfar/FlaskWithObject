from flask_restful import fields

class SingleTransaction:

    def __init__(self,id,balancedue,customerName,startTime):
       self.id = id
       self.balancedue = balancedue
       self.customerName = customerName
       self.startTime = startTime




