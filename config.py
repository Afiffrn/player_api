from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Membuat aplikasi Flask
app = Flask(__name__)

# Konfigurasi database MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://fastapi_whatcropof:a4fb898b609d767a3a00b70c0700b96b33affb6e@tnjkw.h.filess.io:3305/fastapi_whatcropof'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi objek database
db = SQLAlchemy(app)
@app.route('/')
def home():
    return "NAMA    : AFIF FRIZKIANTO NUGROHO
            NIM     : 21.83.0652
            KELAS   : 21TK02
            PRODI   : TEKNIK KOMPUTER"

app.app_context().push()
