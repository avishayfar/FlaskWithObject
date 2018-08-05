from flask_restful import fields

class SingleTransaction:

    def __init__(self,columnsNameLst, valuesLst):
       self.ColumnsNames = columnsNameLst
       self.Values = valuesLst
