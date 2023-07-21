from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from psycopg2.extras import RealDictCursor
import time
#import .config import settings
from .config import settings


SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}'
#SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:password123@localhost:5432/fastapi'


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Commented because now using SQLALCHEMY
# while True:

#      try:
#        conn = psycopg2.connect(host='localhost', database='fastapi', user='postgres', password='Pacer1980', cursor_factory=RealDictCursor)
#        cursor = conn.cursor()
#        print("Databae connection was sucessfull!")
#        break
#      except Exception as error:
#        print("Connection to database failed")
#        print("Error: ", error)
#        time.sleep(2)
    