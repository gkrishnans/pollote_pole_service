from flask import Flask
from myservice import database
from myservice.routes.create_poll import create
from myservice.routes.vote_poll import vote
from myservice.routes.get_user import mypolls
from myservice.routes.get_poll_with_id import get_poll_id
from myservice.routes.get_poll_with_category import polls_category

def create_app():
    app = Flask(__name__)
    app.register_blueprint(create, url_prefix='/api/polls/')
    app.register_blueprint(vote, url_prefix='/api/polls/')
    app.register_blueprint(polls_category, url_prefix='/api/polls/')
    app.register_blueprint(mypolls, url_prefix='/api/polls/')
    app.register_blueprint(get_poll_id,url_prefix='/api/polls/')

    return app

if __name__ == '__main__':
    app = create_app()
    app.debug = True
    app.run(host="localhost", port=6000)

