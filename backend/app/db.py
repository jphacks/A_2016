from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

# TODO: get from env
SQLALCHEMY_DATABASE_URL = "postgresql://pizza:pizzatabetai@postgres/pizza"


def new_db() -> Session:
    engine = create_engine(SQLALCHEMY_DATABASE_URL)
    session_local = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    db = session_local()
    try:
        yield db
    finally:
        db.close()
    return db
