from flask_sqlalchemy import SQLAlchemy
from faker import Faker
db = SQLAlchemy()
# class User(db.Model):
#     pass
class Destination(db.Model):
    __tablename__ = 'destinations'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    safety_rating = db.Column(db.Integer, nullable=False)
    activities = db.Column(db.String(500), nullable=False)
    image = db.Column(db.String(500), nullable=False)
    # reviews = db.relationship('Review', backref='destination', lazy=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    # wishlists = db.relationship('Wishlist', backref='destination', lazy=True)

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'category': self.category,
            'safety_rating': self.safety_rating,
            'activities': self.activities,
            'image': self.image,
            'created_at': self.created_at,
        }


# class Guide():
#     pass
# class Review():
#     pass
# class wishlist():
#     pass