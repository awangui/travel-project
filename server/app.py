#!/usr/bin/env python3
from flask import Flask, request, make_response, jsonify
from flask_cors import CORS
from flask_migrate import Migrate
from models import db,Destination

# Create the Flask app
app = Flask(__name__)
DATABASE_URL= "postgresql://postgres.jtldhkyanvssuoeceppo:nDJpUjslPIouNVPd@aws-0-us-west-1.pooler.supabase.com:5432/postgres"
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False
CORS(app)
migrate = Migrate(app, db)

# Initialize the database
db.init_app(app)

@app.route('/destinations', methods=['GET'])
def destinations():
    if request.method == 'GET':
        destinations = Destination.query.all()

        return make_response(
            jsonify([destination.to_dict() for destination in destinations]),
            200,
        )

    return make_response(
        jsonify({"text": "Method Not Allowed"}),
        405,
    )

if __name__ == '__main__':
    app.run(port=5555)
