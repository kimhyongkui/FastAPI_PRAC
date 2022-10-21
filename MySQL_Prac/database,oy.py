from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

user_name = 'root'
user_pwd = '0000'
db_host = '127.0.0.1'
db_name = 'prac'

SQLALCHEMY_DATABASE_URL = 'mysql+pymysql://root:1234@localhost:3306/prac'




