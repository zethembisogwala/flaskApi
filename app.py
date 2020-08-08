from flask import Flask, jsonify
from flask_restplus import Api, Resource

app = Flask(__name__)
api = Api()

api.init_app(app)


@api.route('/api', '/api/')
class GetAndPost(Resource):

    def get(self):
        return jsonify({'message': 'GET all successfull', 'objects': ['dfe', 'vev', 'vfvwvvv']})

    def post(self):
        data = api.payload
        return jsonify({'message': 'POST successful', 'object': data})


@api.route('/api/<idx>')
class GetUpdateAndDelete(Resource):

    def get(self, idx):
        return jsonify({'message': 'GET by id successful'})

    def put(self, idx):
        data = api.payload
        return jsonify({'message': 'PUT successful', 'object': data})

    def delete(self, idx):
        return jsonify({'message': 'DELETE successful', 'objectId': idx})

@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
