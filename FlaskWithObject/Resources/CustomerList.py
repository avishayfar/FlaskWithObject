from flask_restful import Resource
from Customer import Customer


c1 = SingleCustomer(4, ['a1','b1','c1','d1'])
c2 = SingleCustomer(3, ['a2','b2','c2'])
c3 = SingleCustomer(2, ['a3','b3'])
c4 = SingleCustomer(3, ['a4','b4','c4'])


dict = {'Yossi': c1, 'Ruti': c2, 'Dani': c3 , 'Toto':c4}
customers = Customers(dict)

def abort_if_Customer_doesnt_exist(customerId):
    if customerId not in customers.Ids:
        abort(404, message="Customer {} doesn't exist".format(customerId))

parser = reqparse.RequestParser()
parser.add_argument('customer')

class CustomerList(Resource):
    def get(self):
        @marshal_with(resource_fields)
        def get(self, **kwargs):
             return customers

    def post(self):
        args = parser.parse_args()
        todo_id = int(max(TODOS.keys()).lstrip('todo')) + 1
        todo_id = 'todo%i' % todo_id
        TODOS[todo_id] = {'task': args['task']}
        return True,201