from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()

url = os.getenv("URLPOSTGRES")

SQLALCHEMY_DATABASE_URL = "postgresql://postgress_himw_user:qfzkhkToFjwg7GmqslLUbOydPsUGBCvK@dpg-cs8i3b5svqrc73brv8u0-a.oregon-postgres.render.com/postgress_himw"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()