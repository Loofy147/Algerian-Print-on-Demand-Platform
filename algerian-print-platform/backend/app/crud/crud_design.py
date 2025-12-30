from sqlalchemy.orm import Session

from app.models.design import Design
from app.schemas.design import DesignCreate

def create_with_owner(db: Session, obj_in: DesignCreate, owner_id: int, image_url: str):
    db_obj = Design(
        prompt=obj_in.prompt,
        owner_id=owner_id,
        image_url=image_url
    )
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj
