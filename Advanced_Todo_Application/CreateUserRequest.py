from pydantic import BaseModel


class CreateUserRequest(BaseModel):
    username: str
    email: str
    first_name: str
    surname: str
    password: str
    role: str