import os
from db import db, migrate
from flask import Flask
from models import *
from dotenv import load_dotenv
from auth import login_manager
from controllers import user_bp, tarefa_bp


app = Flask(__name__)


load_dotenv()
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

app.register_blueprint(tarefa_bp)
app.register_blueprint(user_bp)

with app.app_context():
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
