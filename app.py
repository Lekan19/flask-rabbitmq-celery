from flask import Flask, request, jsonify, make_response
from flask_restx import Api, Resource
#from celerytask.tasks import add, celery_app
from celery import Celery

app = Flask(__name__)
api = Api(app)

celery_app = Celery('tasks', broker='amqp://user:nopassword@rabbitmq:5672/addition', backend='rpc://')
@celery_app.task
def add(x, y):
    return x + y

@api.route('/api/addition')
class Addition(Resource):
    def post(self):

        data = request.get_json()
        print(data)
        first_value = data['x']
        second_value = data['y']

        result = add.apply_async(args=(first_value, second_value))
        print(result)
        task_id = result.id
        print(task_id)

        # i want to send this value to a celery app to do the addition
        # return jsonify(data)
        return {"task_id": task_id}, 202


@api.route('/api/status/<string:task_id>')
class Get_Result(Resource):

    def get(self, task_id):
        task = add.AsyncResult(task_id)

        return {"Result": task.status}

        #return make_response(jsonify({"Result": task.status}), 200)

@api.route("/api/result/<string:task_id>")
class Get_Result(Resource):

    def get(self, task_id):

        task = add.AsyncResult(task_id)


        return {"Result": task.get()}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port='8000')