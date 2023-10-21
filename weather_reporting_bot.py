from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import requests

TOKEN: Final = "6759786585:AAExb1hqp9CbJFcIOya090AU_5FjKpn2ivM"
BOT_USERNAME: Final = "@Weather_Land_Bot"

BASE_URL: Final = "http://api.openweathermap.org/data/2.5/weather?"
API_KEY: Final = "8438a0ea83aa941f5c4f746f15f95c26"

# Commands


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hi! I am a meteorological robot")


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("If you add me to a group, I will send a text message about the weather in Tehran every ten minutes. If you want to know about the weather condition of another city, you can send me the name of the city you want in P.V., or mention me in a message in the group and write the name of that city :)")


# Handle Message
async def handle_messages(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: update.message.chat.type
    city = update.message.text.strip()

    if message_type == "group":
        if BOT_USERNAME in city:
            target_city = city.replace(BOT_USERNAME, "").strip()
            city = target_city

    city = "New York"
    url = BASE_URL + "appid=" + API_KEY + "&q=" + city
    response = requests.get(url).json()

    def kelvin_to_celsius(kelvin): return kelvin - 273.15
    temp_kelvin = response["main"]["temp"]
    temp_celsius = kelvin_to_celsius(temp_kelvin)

    feels_like_kelvin = response["main"]["feels_like"]
    feels_like_celsius = kelvin_to_celsius(feels_like_kelvin)

    humidity = response["main"]["humidity"]

    description = response["weather"][0]["description"]

    wind_speed = response["wind"]["speed"]

    result = city + "\t" + temp_celsius + "°C\t" + description + "\nHumidity: " + humidity + "\nWind speed: " + wind_speed + "km/h" + "\nFeels like: "  + feels_like_celsius +"°C"
    await update.message.reply_text(result)

