from flask import Flask
from db import DATABASE_URI, db, migrate
from auth import login_manager
from controllers import tarefa_bp, user_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URI
app.config['SECRET_KEY'] = 'supersecret'

# Routes
app.register_blueprint(tarefa_bp)
app.register_blueprint(user_bp)

with app.app_context():
    db.init_app(app)
    migrate.init_app(app)
    login_manager.init_app(app)

if __name__ == "__main__":
    app.run(debug=True)
