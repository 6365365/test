from pydantic import BaseModel, validator


class SchemaPhoneData(BaseModel):
    phone: str
    address: str

    @validator('phone')
    def phone_validation(cls, phone) -> str:
        try:
            phone.alnum()
        except AttributeError:
            raise ValueError(f'Wrong phone number')
        return phone
