from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps
from app.services import ml_service

router = APIRouter()

@router.post("/", response_model=schemas.Design)
def create_design(
    *,
    db: Session = Depends(deps.get_db),
    design_in: schemas.DesignCreate,
    current_user: models.User = Depends(deps.get_current_user),
):
    """
    Create new design.
    """
    image_url = ml_service.generate_mock_image(prompt=design_in.prompt)
    design = crud.design.create_with_owner(
        db=db, obj_in=design_in, owner_id=current_user.id, image_url=image_url
    )
    return design
