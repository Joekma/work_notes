from flask import Flask,request
from flask_restful import Resource,Api


app = Flask(__name__)
api = Api(app)


# class HelloWorld(Resource):
#     def get(self):
#         return {'hello':'world'}
#
# api.add_resource(HelloWorld,"/")

# curl http://127.0.0.1:5000/


todos ={}

class ToDoSimple(Resource):
    def get(self,todo_id):
        return {todo_id:todos[todo_id]}

    def put(self,todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id:todos[todo_id]}

api.add_resource(ToDoSimple,'/<string:todo_id>')













if __name__ == '__main__':
    app.run(debug=True)

