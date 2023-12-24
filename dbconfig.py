from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Specify the details for the database connection with username root and password root123 and ip 20.110.164.241
username = 'root'
password = 'root123'
server = '20.110.164.241'
port = '3306'
database_name = 'userdb'

DATABASE_URL = f"mysql+pymysql://{username}:{password}@{server}:{port}/{database_name}"

# Create a SQLAlchemy engine
engine = create_engine(DATABASE_URL)

# Create a SQLAlchemy ORM session factory bound to this engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for our classes definitions
Base = declarative_base()
