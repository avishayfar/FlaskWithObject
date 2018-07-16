from flask_restful import Resource

class Customer(Resource):
    def get(self, customerId):
        abort_if_Customer_doesnt_exist(customerId)
        @marshal_with(resource_fields)
        def get(self, **kwargs):
            return customers.GetCustomer(customerId)

    def delete(self, customerId):
        abort_if_Customer_doesnt_exist(customerId)
        customers.DeleteCustomer(customerId)
        return '', 204

    def put(self, customerId):
        args = parser.parse_args()
        customer = {'task': args['task']}
        TODOS[todo_id] = task
        return task, 201
