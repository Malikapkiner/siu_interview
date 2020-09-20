from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#TODO: Hide this
#Connection string for database connection. 
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:malimali123@localhost:5432/siu3"

#SQLAlchemy connection engine.
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

#This base will used for model classes.
Base = declarative_base()