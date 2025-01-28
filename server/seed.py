from app import app
from models.models import db, Destination  

def add_fake_data():
    destinations = [
        Destination(name="Paris", description="City of Light", category="City", safety_rating=5, activities="Eiffel Tower, Louvre Museum, Notre-Dame Cathedral", image="https://images.unsplash.com/photo-1533227268428-f4e0f59b8f6c"),
        Destination(name="Tokyo", description="Capital of Japan", category="City", safety_rating=4, activities="Tokyo Tower, Senso-ji Temple, Meiji Shrine", image="https://images.unsplash.com/photo-1533227268428-f4e0f59b8f6c"),
        Destination(name="Sydney", description="Largest city in Australia", category="City", safety_rating=5, activities="Sydney Opera House, Sydney Harbour Bridge, Bondi Beach", image="https://images.unsplash.com/photo-1533227268428-f4e0f59b8f6c"),
        Destination(name="Bora Bora", description="Island in French Polynesia", category="Island", safety_rating=4, activities="Matira Beach, Mount Otemanu, Coral Gardens", image="https://images.unsplash.com/photo-1533227268428-f4e0f59b8f6c"),

    ]

    with app.app_context():  # Use the app context
        db.session.bulk_save_objects(destinations)  # Add multiple records at once
        db.session.commit()
        print("Fake data added successfully!")

if __name__ == "__main__":
    add_fake_data()
