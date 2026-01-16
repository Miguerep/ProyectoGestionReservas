import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from src.common import db, Cliente, Servicio, Cita, Peluqueria, Estilista, CitaServicio, PeluqueriaServicio
from src.backend.routes import api

load_dotenv()

app = Flask(__name__)
CORS(app)
user = os.getenv("DB_USER")
passwd = os.getenv("DB_PASSWORD")
host = os.getenv("DB_HOST")
db_name = os.getenv("DB_NAME")
port = os.getenv("DB_PORT")

app.config["SQLALCHEMY_DATABASE_URI"] = f"mysql+pymysql://{user}:{passwd}@{host}:{port}/{db_name}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

db.init_app(app)

with app.app_context():
    db.create_all()
    print("Tablas sincronizadas en " + db_name)
    
    
app.register_blueprint(api)

@app.route('/')
def index():
    return {"status": "ok", "message": "API CutTime Online"}


if __name__ == '__main__':
    app.run(debug=True, port=5000)