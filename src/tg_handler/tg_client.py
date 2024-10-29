from telethon import TelegramClient
from src.config.config_files import Settings


def get_telegram_client():
    """
    Creates and returns a TelegramClient instance.

    Returns:
        TelegramClient: The initialized TelegramClient instance.
    """

    api_id = Settings.TG_API_ID
    api_hash = Settings.TG_API_HASH

    client = TelegramClient('session_name', api_id, api_hash)
    client.start()

    return client