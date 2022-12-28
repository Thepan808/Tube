""" !/usr/bin/env python3
    -*- coding: utf-8 -*-
    Name     : inline-tube-mate [ Telegram ]
    Repo     : https://github.com/m4mallu/inine-tube-mate
    Author   : Renjith Mangal [ https://t.me/space4renjith ]
    Credits  : https://github.com/SpEcHiDe/AnyDLBot """

import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S'
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):
    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5612901649:AAHm5GgcpXuXs57zRGR4JzzbB94ouYU8IiU")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "4954361"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "43a786a8548a30f9d6887e36d53c0e64")

    # Authorized user ids to use this bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "").split())

    # superusers to broadcast messages & fetch subscribers count
    SUDO_USERS = set(int(x) for x in os.environ.get("SUDO_USERS", "").split())

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "postgres://jhcpwcku:7S_eIC5qrzn4LlanVdRIz7PPLYlkeBTP@motty.db.elephantsql.com/jhcpwcku")

    # Force subscribe channel / group id starting with -100
    FORCE_SUB_CHAT = os.environ.get("FORCE_SUB_CHAT", "1613249033")

    # Telegram maximum file upload size
    TG_MAX_FILE_SIZE = 2097152000

def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
