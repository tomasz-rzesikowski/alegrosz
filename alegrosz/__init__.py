from flask import Flask, g


def create_app():
    alegrosz = Flask(__name__)

    alegrosz.config.from_object('alegrosz.config.DevelopmentConfig')

    from .views import bp_main
    from .views import bp_item

    alegrosz.register_blueprint(bp_main)
    alegrosz.register_blueprint(bp_item)

    @alegrosz.teardown_appcontext
    def close_connection(exception):
        db = getattr(g, '_database', None)
        if db is not None:
            db.close()

    return alegrosz
