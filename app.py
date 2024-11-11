from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Now you can access environment variables
secret_key = os.getenv('FLASK_SECRET_KEY')
database_uri = os.getenv('DATABASE_URI')

# Example Flask app setup
from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = secret_key
app.config['SQLALCHEMY_DATABASE_URI'] = database_uri

@app.route('/')
def home():
    return "Hello, World!"

if __name__ == "__main__":
    app.run()
