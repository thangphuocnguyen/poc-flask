from flask import Flask, Blueprint
from flask_restful import Api

from tpnapi.resources.todo import Todo, TodoList

def create_app(config_object='tpnapi.settings'):
    """
    Create app
    """

    # app initiliazation
    app = Flask(__name__)

    app.config.from_object(config_object)

    api_bp = Blueprint('api', __name__)
    api = Api(api_bp)

    api.add_resource(TodoList, '/todos')
    api.add_resource(Todo, '/todos/<todo_id>')

    app.register_blueprint(api_bp)

    return app
