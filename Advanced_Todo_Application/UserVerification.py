from pydantic import Field, BaseModel


class UserVerification(BaseModel):
    password: str
    new_password: str = Field(min_length=8)
