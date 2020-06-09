from flask import Flask, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app) 

class Ping(Resource):
    def get(self):
        json_ret = {
                'msg': 'pong'
                }
        return jsonify(json_ret)

api.add_resource(Ping, '/ping')

if __name__ == '__main__':
    app.run()
