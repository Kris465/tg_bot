import os

from playwright.sync_api import sync_playwright
from loguru import logger
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv)

LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')
logger.info("Запуск браузера...")

with sync_playwright() as p:
    logger.add('file.log',
               format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
               rotation="3 days")

    brower = p.chromium.launch(headless=False)
    page = brower.new_page()

    page.goto("https://omni.top-academy.ru/login/index#/")
    logger.info("Страница загружена")

    input("Нажмите Enter для закрытия...")
    brower.close()
