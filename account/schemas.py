from typing import Optional

from ninja import Schema
from pydantic import EmailStr, Field, UUID4


class AccountCreate(Schema):
    first_name: str = Field(min_length=2)
    last_name: str = Field(min_length=2)
    email: EmailStr
    password1: str = Field(min_length=8)
    password2: str = Field(min_length=8)
    #image: str



class AccountOut(Schema):
    id: UUID4
    first_name: str
    last_name: str
    email: EmailStr
    #image: str
    phone_number: Optional[str]
    address1: str = None
    address2: str = None
    company_name: str = None
    company_website: str = None

class TokenOut(Schema):
    access: str

class AuthOut(Schema):
    token: TokenOut
    account: AccountOut

class SigninSchema(Schema):
    email: EmailStr
    password: str




class AccountUpdate(Schema):
    first_name: str
    last_name: str
    phone_number: Optional[str]
    address1: str
    address2: str
    company_name: str
    company_website: str
    #image: str


class ChangePasswordSchema(Schema):
    old_password: str
    new_password1: str
    new_password2: str
