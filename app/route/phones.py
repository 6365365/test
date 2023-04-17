from fastapi import APIRouter, Depends
from app.core.phones import write_phone, check_phone
from app.shemas.phones import SchemaPhoneData


phones_route = APIRouter()


@phones_route.get('/check_data')
async def check_data(phone: str):
    return await check_phone(phone=phone)


@phones_route.post('/write_data')
async def save_user_data(data: SchemaPhoneData):
    return await write_phone(data=data)
