"""
Solidware DevOps Task
Author: YoungHO Kim
Reference : Book(Building RESTful Python Web Services) Chapter 5-2
"""
from flask import Flask
from flask import jsonify
from flask_restful import abort, Api, reqparse, Resource

import model
import status
from photo import Photo


class PredictionManager:
    last_id = -1

    def __init__(self):
        self.photos = {}

    def insert_photo(self, photo):
        self.__class__.last_id += 1
        photo.id = self.__class__.last_id
        photo.age = model.predict_age(photo.url)
        self.photos[self.__class__.last_id] = photo
        return photo

    def get_photo(self, id):
        return self.photos[id]

    def delete_photo(self, id):
        del self.photos[id]


prediction_manager = PredictionManager()


class Predictions(Resource):
    def abort_if_identification_doesnt_exist(self, id):
        if id not in prediction_manager.photos:
            abort(
                status.HTTP_404_NOT_FOUND,
                message="Message {0} doesn't exist".format(id))

    def post(self):
        """
            The /predictions API should accept POST requests with a JSON request body.
            The JSON request must have the following format:
            {"url":"https://host.com/some/image.jpg"}
            The url value should be used as an argument to the ​model.py​ script to get the predicted age.
            The server should respond with a JSON response body with the following format:
            {"id": 1234}
            The id should be a unique value for every request. The id can either be a string or an integer.
        """
        parser = reqparse.RequestParser()
        parser.add_argument('url', type=str, required=True, help='Url cannot be blank!')
        args = parser.parse_args()
        photo = Photo(
            url=args['url']
        )
        new_photo = prediction_manager.insert_photo(photo)
        return jsonify(id=new_photo.id)

    def get(self, id):
        """
            The /predictions/<id> API should accept GET requests and return a JSON response body.
            The <id> part of the URL should be replaced with an id value that was previously returned from POSTing to the /predictions API.
            The response body should have the following format:
            {"age": 42}
            The age value can be an integer or null. The age value should be the output from the model.py​ script.
        """
        if id is None:
            print("-------->")
        self.abort_if_identification_doesnt_exist(id)
        return jsonify(age=prediction_manager.get_photo(id).age)


app = Flask(__name__)
api = Api(app)
api.add_resource(Predictions, '/predictions', '/predictions/<int:id>')

if __name__ == '__main__':
    app.run(debug=True)
