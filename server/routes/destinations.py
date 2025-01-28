from flask import Flask, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models.models import db
from routes.destinations import destinations_bp

# Create the Flask app
app = Flask(__name__)
DATABASE_URL= "postgresql://postgres.jtldhkyanvssuoeceppo:nDJpUjslPIouNVPd@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

CORS(app)

# Initialize the database and migrations
db.init_app(app)
migrate = Migrate(app, db)

# Register blueprints
app.register_blueprint(destinations_bp, url_prefix='/api')

# Define a route for the root URL
@app.route('/')
def index():
    return jsonify({"message": "Welcome to the WanderWith API"})

if __name__ == '__main__':
    app.run(port=5555)
