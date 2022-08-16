from pydantic import BaseModel

class UserBase(BaseModel):
    username: str
    email: str
    password: str

class UserDisplay(BaseModel):
    username: str
    email: str
    # Automates the process of converting our DB data automatically
    # into the form we describe above
    class Config():
        orm_mode = True