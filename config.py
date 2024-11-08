from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Membuat aplikasi Flask
app = Flask(__name__)

# Konfigurasi database MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://playerapi_sleptspin:8351a41631006ade17e583976fc426bdc504f722@e6uht.h.filess.io:3305/playerapi_sleptspin'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inisialisasi objek database
db = SQLAlchemy(app)
@app.route('/')
def home():
    return "hello world!!!"

app.app_context().push()
