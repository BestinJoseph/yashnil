from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(f'postgresql://postgres:jefF1234@localhost:5432/yashnil_db')

session = sessionmaker(bind=engine)

Base = declarative_base()