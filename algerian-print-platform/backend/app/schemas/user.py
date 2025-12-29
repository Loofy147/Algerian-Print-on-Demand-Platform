from pydantic import BaseModel, EmailStr, ConfigDict

# Shared properties
class UserBase(BaseModel):
    email: EmailStr

# Properties to receive via API on creation
class UserCreate(UserBase):
    password: str

# Properties to return to client
class User(UserBase):
    id: int
    is_active: bool

    model_config = ConfigDict(from_attributes=True)

# Properties stored in DB
class UserInDB(User):
    hashed_password: str
