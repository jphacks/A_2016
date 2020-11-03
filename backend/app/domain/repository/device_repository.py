from sqlalchemy.orm import Session

from app.domain import schemas, entity


def create_device(db: Session, device: schemas.DeviceCreate):
    db_device = entity.Device(
        id=device.id,
        item=device.item,
        max=device.max,
        min=device.min,
    )

    db.add(db_device)
    db.commit()
    db.refresh(db_device)
    return db_device
