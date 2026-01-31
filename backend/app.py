import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv # pip install python-dotenv

# 1. Cargar variables de entorno
load_dotenv()

from src.common import db
from src.backend.routes import api

app = Flask(__name__)
CORS(app)

# 2. Configuración Segura
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cuttime.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# ¡JAMÁS HARDCODED! Lee de .env o usa una default solo en dev
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "fallback-secret-solo-para-dev")

jwt = JWTManager(app)
db.init_app(app)

app.register_blueprint(api)

# 3. Global Error Handler
@app.errorhandler(Exception)
def handle_exception(e):
    # Loguear el error real en servidor
    print(f" ERROR 500: {str(e)}")
    return {"msg": "Error interno del servidor", "error": str(e)}, 500

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)