# Telegram Feedback bot

Feedback Bot is designed for easy and anonymous communication with Telegram users. With this bot, users can submit questions or feedback, and you can respond by simply replying to their messages within the bot. This project is powered by Aiogram and requires the use of a MySQL database.

![](https://github.com/matt-novoselov/Feedback-Telegram-Bot/blob/ca940ac3af5c2b98faa5f593621e0031c8261556/Thumbnail.png)


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
