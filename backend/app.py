import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

# 1. Cargar el archivo .env
load_dotenv()

from src.common import db
from src.backend.routes import api

app = Flask(__name__)
CORS(app)


db_user = os.getenv("DB_USER")
db_pass = os.getenv("DB_PASSWORD")
db_host = os.getenv("DB_HOST")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DB_NAME")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["JWT_SECRET_KEY"] = os.getenv("SECRET_KEY") 

jwt = JWTManager(app)
db.init_app(app)

app.register_blueprint(api)

# Manejador de errores global
@app.errorhandler(Exception)
def handle_exception(e):
    print(f"ERROR: {e}")
    return {"msg": "Error interno del servidor", "error": str(e)}, 500

if __name__ == "__main__":
    # Creamos las tablas si no existen (solo para desarrollo)
    with app.app_context():
        db.create_all()
    app.run(
        debug=os.getenv("FLASK_DEBUG") == "1",
        port=int(os.getenv("API_PORT", 5000))
    )