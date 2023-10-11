import os

from flask import Flask

"""
Instead of creating a Flask instance globally, you will create it inside a function.
This function is known as the application factory.
Any configuration, registration, and other setup the application needs will happen inside the function, then the application will be returned.

The __init__.py serves double duty: it will contain the application factory, and it tells Python that the flaskr directory should be treated as a package.
"""

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    # Initialize the Database File
    from . import db
    db.init_app(app)

    return app