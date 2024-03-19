from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
from flask import Flask

app = Flask(__name__)
app.secret_key = '$%^*&())(*&%^%4678675446&#%$%^&&*^$&%&*^&^'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost/joke?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)