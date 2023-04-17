import aioredis
from app.settings import CONFIG

redis = aioredis.from_url(CONFIG.REDIS_URL)
