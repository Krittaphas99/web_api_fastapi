
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi import Depends
import os 
load_dotenv()
host=os.getenv("HOST")
user= os.getenv("USER")
password= os.getenv("PASSWORD") 
database = os.getenv("DATABASE")

engine = create_engine(f"mysql+pymysql://{user}:{password}@{host}:3306/{database}")

Sessionlocal = sessionmaker(autoflush=False,bind=engine)
Base = declarative_base()
# con = engine.connect()
print("hiserver")

def get_db():
  db = Sessionlocal()
  try:
    yield db
  finally:
    db.close()

db_dependency = Annotated[Session, Depends(get_db)]
  

 