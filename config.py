DATABASE = 'ota_db'
USERNAME = 'root'
PASSWORD = 'stxx@1234'
HOST = '36.46.135.93'
PORT = '3306'
# 创建连接和操作数据库的URI
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://{}:{}@{}:{}/{}'.format(USERNAME, PASSWORD, HOST, PORT,
                                                                  DATABASE)
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_ECHO = True

