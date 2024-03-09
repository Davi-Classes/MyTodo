import os
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv


load_dotenv()
DATABASE_URI = os.getenv('DATABASE_URI')

db = SQLAlchemy()
migrate = Migrate(db=db)
