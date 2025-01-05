from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from the .env file

class Config:
    SQLALCHEMY_DATABASE_URI = (
        f"postgresql://{os.getenv('POSTGRES_USER')}:{os.getenv('POSTGRES_PASSWORD')}"
        f"@{os.getenv('POSTGRES_HOST')}:{os.getenv('POSTGRES_PORT')}/{os.getenv('POSTGRES_DB')}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Avoid unnecessary overhead
    FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY") 