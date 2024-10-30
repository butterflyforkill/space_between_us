import asyncio
from telethon import TelegramClient, events
from src.tg_handler.config_files import Settings
from src.cron_rabbitmq import rabbit_mq_handler


def get_telegram_client():
    """
    Creates and returns a TelegramClient instance.

    Returns:
        TelegramClient: The initialized TelegramClient instance.
    """

    api_id = Settings.TG_API_ID
    api_hash = Settings.TG_API_HASH

    client = TelegramClient('session_name', api_id, api_hash)
    client.start(bot_token=Settings.TOKENkey)

    return client


async def handle_start(event):
    user_id = event.sender_id
    first_name = event.sender.first_name or "Unknown"
    last_name = event.sender.last_name or ""
    username = event.sender.username or "Unknown"

    # Store user information, including username
    await rabbit_mq_handler.send_user_info_to_rabbitmq(user_id, username, first_name, last_name)

    await event.respond(f"Hello, {first_name} {last_name} ({username})!")


async def main():
    client = get_telegram_client()
    client.add_event_handler(handle_start, events.NewMessage(pattern='/start'))
    await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())