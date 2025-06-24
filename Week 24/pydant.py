from pydantic import BaseModel, EmailStr, validator

class User(BaseModel):
    name: str
    email: EmailStr
    account_id: int

    @validator("account_id")
    def validate_account_id(cls, value):
        if value<=0:
            raise ValueError(f'accoutn_id must be positive: {value}')
        return value

user = User(name= "Shaurya", email="Shauryavratshukla@gmail.com", account_id= 14232)
print(user)

user_json_str = user.json()
print(user_json_str)

user_json_obj = user.dict()
print(user_json_obj)

json_str = '{"name": "jack", "email": "Jack@test.io", "account_id": 1234}'
user = User.parse_raw(json_str)
print(user)