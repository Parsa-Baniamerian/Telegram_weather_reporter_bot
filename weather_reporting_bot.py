from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN: Final = "6759786585:AAExb1hqp9CbJFcIOya090AU_5FjKpn2ivM"
BOT_USERNAME: Final = "@Weather_Land_Bot"

BASE_URL: Final = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY: Final = "8438a0ea83aa941f5c4f746f15f95c26"
