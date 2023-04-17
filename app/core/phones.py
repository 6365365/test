from app.shemas.phones import SchemaPhoneData
from app.core.redis import redis


async def write_phone(data: SchemaPhoneData):
    return await redis.set(data.phone, data.address)


async def check_phone(phone: str):
    return await redis.get(phone)
