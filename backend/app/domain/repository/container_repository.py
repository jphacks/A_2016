from typing import List

from sqlalchemy.orm import Session

from app.domain import entity


def get_all_containers(db: Session) -> List[entity.Container]:
    return db.query(entity.Container).all()
