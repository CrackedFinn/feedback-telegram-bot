## Telegram Feedback bot

Introducing Telegram Feedback bot, designed for seamless, anonymous communication with users. With this bot, users can submit questions or feedback, and you can effortlessly respond by simply replying to their messages. This bot is powered by Aiogram and leverages a MySQL database.

![](https://github.com/matt-novoselov/Feedback-Telegram-Bot/blob/b133e0f4e1dbb174064f8747de5fdf2afa67b425/Thumbnail.png)

[![Telegram Bot](https://github.com/matt-novoselov/matt-novoselov/blob/4fddb3cb2c7e952d38b8b09037040af183556a77/Files/telegram_button.svg)](https://t.me/NoveSupportBot)

[![Deploy on Railway](https://railway.app/button.svg)](https://railway.app/new/template/UwAyn7?referralCode=RmyABJ)

## Requirements
- Python 3.8
- aiogram 2.25.1
- python-dotenv 1.0.0
- aiomysql 0.1.1

## Installation
1. Clone repository using the following URL: `https://github.com/matt-novoselov/Feedback-Telegram-Bot.git`
2. Create Environment File:
   - Create a file named `.env` in the root directory of the source folder.
   - Use the provided `.env.example` file as a template.
3. Replace the placeholder values with your specific configuration:
   - ADMIN_ID: Telegram User ID of the admin who has access to manage the bot.
   - TOKEN: Insert your Telegram Bot Token obtained from the [BotFather](https://t.me/botfather).
   - HOST: This is the host address for your MySQL database.
   - DB_USERNAME: The username used to access your MySQL database.
   - PASSWORD: The password associated with the provided username for accessing the MySQL database.
   - DATABASE: The name of the MySQL database your bot will use.
4. Build and run `main.py`

<br>

## Credits
Distributed under the MIT license. See **LICENSE** for more information.

Developed with ❤️ by Matt Novoselov
