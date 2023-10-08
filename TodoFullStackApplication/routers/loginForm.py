from typing import Optional
from starlette.requests import Request


class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def create_oauth_form(self):
        form = await self.request.form()

        # In the form, the email is of type text field. OAuth needs the name email for it to properly work.
        self.username = form.get("email")
        self.password = form.get("password")
