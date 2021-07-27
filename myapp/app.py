from flask import Flask

# Importa os blueprints
from myapp.blueprints.site.views import site

# Importa as extensões
from myapp.extensions.debbuger import debug_toolbar

def create_app(conf_externas=None):

    # Carrega as configurações
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    if conf_externas:
        app.config.update(conf_externas)

    # Registra os blueprints
    app.register_blueprint(site)

    # Registra as extensões
    extensions(app)
    return app

def extensions(app):
    """
    Register 0 or more extensions (mutates the app passed in).

    :param app: Flask application instance
    :return: None
    """

    # Extensão de debug
    debug_toolbar.init_app(app)

if __name__ == "__main__":
    create_app()
