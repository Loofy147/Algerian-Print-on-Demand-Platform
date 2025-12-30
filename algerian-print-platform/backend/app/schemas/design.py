from pydantic import BaseModel, ConfigDict

# Shared properties
class DesignBase(BaseModel):
    prompt: str

# Properties to receive via API on creation
class DesignCreate(DesignBase):
    pass

# Properties to return to client
class Design(DesignBase):
    id: int
    image_url: str
    owner_id: int

    model_config = ConfigDict(from_attributes=True)
