from flask import Flask, request
from flask_restful import Resource, Api
from werkzeug.exceptions import BadRequest

app = Flask(__name__)
api = Api(app)

# In-memory data store (for demo purposes)
items = {}

class Item(Resource):
    def get(self, name):
        """Retrieve an item by name."""
        return "Welcome to the App Page!"

    


# Resource routing

api.add_resource(Item, "/")

if __name__ == "__main__":
    app.run(debug=True)
    