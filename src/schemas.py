from pydantic import BaseModel, ConfigDict

class UserBase(BaseModel):
    username: str
    email: str
    model_config = ConfigDict(from_attributes=True)

class UserCreate(UserBase):
    password: str

class User(UserBase):
    id: int
    username: str
    email: str