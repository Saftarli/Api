from flask_restx import Resource,Namespace


order_namespace = Namespace('orders', description="Namspace for orders")



@order_namespace.route('/')
class HelloOrders(Resource):
    

    def get(self):
        return{ "message ": "Hello orders"}