from flask import Flask
from app.routes import cens_blueprint

app = Flask(__name__)

if __name__ == "__main__": 
    app.register_blueprint(cens_blueprint)
    app.run() 