from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session
from gino import Gino

DB_DSN = "postgres://user:password@localhost:5432/typicode"

db = Gino()

engine = create_engine(DB_DSN, echo=True)
Base = declarative_base(bind=engine)

session_factory = sessionmaker(bind=engine)
Session = scoped_session(session_factory)
