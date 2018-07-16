from flask_restful import fields

class SingleTransaction:

    def __init__(self,id,balancedue,customerName,startTime):
       self.id = id
       self.balancedue = balancedue
       self.customerName = customerName
       self.startTime = startTime


class SingleCustomer:

    def __init__(self,stam,list=None):
        self.stam = stam
        if list is None:
            list = []
        self.list = list()
    

    def __str__(self):
        return ('_'.join(self.list))

    def len(self):
        return len(self.list)

class Customers:

    def __init__(self, dictOfCustomers):
        self.dictOfCustomers = dictOfCustomers

    def show(self):
        for k,v in self.dictOfCustomers.items():
            print(k, '-', v)

    def GetCustomer(self,key):
        return self.dictOfCustomers[key]

    def UpdateCustomer(self,key,SingleCustomer):
        self.dictOfCustomers[key] = SingleCustomer

    def DeleteCustomer(self,key):
        self.dictOfCustomer

    def Ids(self):
        return self.dictOfCustomers.keys()

