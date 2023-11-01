# WeatherLand Telegram Bot

WeatherLand Telegram Bot is a Python bot that provides real-time weather information for cities using the OpenWeatherMap API. Users can request weather information by sending the name of a city in a private message or mentioning the bot in a group chat and specifying the city name.

### Features

- Get current weather conditions for any city.
- Real-time updates on temperature, humidity, wind speed, and more.
- User-friendly commands for easy interaction.

### Usage

1. Start a chat with the bot by sending a private message.
2. Use the following commands to interact with the bot:

    - `/start`: Start a conversation with the bot.
    - `/help`: Learn how to request weather information for a specific city.

3. To get weather information for a city, either send the city name directly or mention the bot in a group chat followed by the city name (e.g., `@Weather_Land_bot New York`).

### Installation

To run this bot, you need to create a `set.conf` file and provide the necessary API keys and token. Make sure to have a valid OpenWeatherMap API key and a Telegram Bot Token. Example `set.conf` file:

```ini
[BOT]
TOKEN = your_telegram_bot_token
USERNAME = your_bot_username

[API]
API_KEY = your_openweathermap_api_key
```

Install the required Python packages using pip:

```shell
pip install python-telegram-bot requests
```

Finally, run the bot:

```shell
python your_bot_file.py
```
Replace your_telegram_bot_token and your_openweathermap_api_key with your actual credentials in the set.conf file. Make sure to provide the appropriate file name for your bot's Python code in the last command (python your_bot_file.py).


### Dependencies

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot): Python wrapper for the Telegram Bot API.
- [requests](https://docs.python-requests.org/en/master/): Library for making HTTP requests.


### Acknowledgments

Special thanks to the developers of the [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) library and the [OpenWeatherMap API](https://openweathermap.org/) for their services.




