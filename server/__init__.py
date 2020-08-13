from flask import Flask
from sassutils.wsgi import SassMiddleware

from instance.config import app_config
from server.extensions import Base, engine

from server.root.views import root_blueprint
from server.house.views import house_blueprint

def create_app(config_name) :
    app = Flask(__name__)
    
    Base.metadata.create_all(engine)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('../instance/config.py')

    app.wsgi_app = SassMiddleware(app.wsgi_app, {
        'server': ('static/sass', 'static/css', '/static/css')
    })

    app.register_blueprint(root_blueprint)
    app.register_blueprint(house_blueprint)

    return app