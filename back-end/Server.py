"""
    Micro Server For CAUP Front End
"""
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/signup', methods=['POST'])
def sign_up():
    """
        Accept the sign up post request
    """
    pass
