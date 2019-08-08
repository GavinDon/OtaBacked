import os

from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import config
from sqlalchemy.orm import scoped_session  # 线程安全
from flask_sqlalchemy import SessionBase


'''
初始化 app 实例和 sql
'''
app = Flask(__name__)
CORS(app, supports_credentials=True)
app.config.from_object(config)
# secret_key = os.urandom(24)
secret_key = b'\x05\xb6&[7)\xdb\xe4~\xf5V\xea\x92\x0f,8^\xc9\x80#jV(\xa4'
app.config['SECRET_KEY'] = secret_key

db = SQLAlchemy()
db.init_app(app)
