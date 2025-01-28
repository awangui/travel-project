#!/usr/bin/env python3
#serves as the main entry point
from flask import Flask
from flask_cors import CORS
from flask_migrate import Migrate
from models.models import db
from routes.destinations import destinations_bp
from dotenv import load_dotenv

import os

load_dotenv()

# Create the Flask app
app = Flask(__name__)

DB_CONFIG = {
    "dbname":os.getenv("DB_NAME"),
    "user":os.getenv("DB_USER"),
    "password":os.getenv("DB_PASSWORD"),
    "host":os.getenv("DB_HOST"),
    "port":os.getenv("DB_PORT")
}

DATABASE_URL= f"postgresql://{DB_CONFIG['user']}:{DB_CONFIG['password']}@{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['dbname']}"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

# Initialize the database and migrations
db.init_app(app)
migrate = Migrate(app, db)

#register blueprints
app.register_blueprint(destinations_bp, url_prefix='/api')

if __name__ == '__main__':
    app.run(port=5555)
