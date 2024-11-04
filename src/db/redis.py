import redis.asyncio as aioredis
from src.config.config_files import Settings


JTI_EXPIRY = 3600

token_blocklist = aioredis.from_url(
    Settings.REDIS_URL
)


async def add_jti_to_blocklist(jti: str) -> None:
    await token_blocklist.set(
        name=jti,
        value="",
        ex=JTI_EXPIRY
    )


async def token_in_blocklist(jti: str) -> bool:
    return await token_blocklist.get(jti) is not None