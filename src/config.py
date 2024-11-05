import os

class Config:
    """Configuration for the Flask application."""
    SECRET_KEY = 'your_secret_key_here'  # Use a proper secret key in production
    # You can also add other config variables like database URIs, etc.
    DATABASE_URI = os.path.join(os.getcwd(), 'data', 'anitrac.db')