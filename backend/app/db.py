from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session

# TODO: get from env
DATABASE_URL = "postgresql://pizza:pizzatabetai@postgres/pizza"
Base = declarative_base()


def new_db() -> Session:
    global Base
    engine = create_engine(DATABASE_URL)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_local()
    try:
        yield db
    finally:
        db.close()
    return db
