from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import os
from dotenv import load_dotenv
import mysql_database

# Load secrets from environment
load_dotenv()

# Get bot token for API
bot = Bot(token=os.getenv('TOKEN'))

# Get admin Telegram ID
admin_id = os.getenv('ADMIN_ID')
dp = Dispatcher(bot)


# Run after /start command
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("🛠️ *Hi!*\n\nWrite your question here and we will answer it as soon as possible.",
                         parse_mode="Markdown")


# Run after /ban command
@dp.message_handler(commands=['ban'])
async def ban_user(message: types.Message):
    # USER EXPERIENCE
    if int(message.chat.id) != int(admin_id):
        await message.answer("You can't use this command", parse_mode="Markdown")
    # ADMIN EXPERIENCE
    else:
        if message.reply_to_message:
            # Extract Telegram ID from the message
            if message.reply_to_message.content_type == 'text':
                extractedID = message.reply_to_message.text.split("#")[-1]
            else:
                extractedID = message.reply_to_message.caption.split("#")[-1]
            await mysql_database.BanUser(extractedID)
            await message.answer(f"User {extractedID} was successfully banned.", parse_mode="Markdown")
        else:
            await message.answer("Reply to a particular message to answer it", parse_mode="Markdown")


# Handle all content types that user sends
@dp.message_handler(content_types=types.ContentType.all())
async def text_message(message: Message):
    # Types of content that can be forwarded
    supported_content_types = ['document', 'text', 'photo', 'audio', 'video', 'animation']
    if message.content_type not in supported_content_types:
        await message.answer(
            f"Sorry, your message wasn't delivered. You can't send {message.content_type} to the Support bot.",
            parse_mode="Markdown")
    else:
        # USER EXPERIENCE
        if int(message.chat.id) != int(admin_id):
            myresult = await mysql_database.CheckUser(message.chat.id)
            if len(myresult) > 0:  # User is banned
                await message.answer("You were banned from the bot.", parse_mode="Markdown")
            else:
                if message.content_type == 'text':
                    await bot.send_message(chat_id=admin_id, text=message.text + f"\n\n#{message.chat.id}")
                else:
                    await bot.copy_message(chat_id=admin_id, message_id=message.message_id,
                                           from_chat_id=message.chat.id,
                                           caption=f"#{message.chat.id}")

        else:  # ADMIN EXPERIENCE
            if message.reply_to_message:
                # Extract Telegram ID from the message
                if message.reply_to_message.content_type == 'text':
                    extractedID = message.reply_to_message.text.split("#")[-1]
                else:
                    extractedID = message.reply_to_message.caption.split("#")[-1]
                try:
                    await bot.copy_message(chat_id=extractedID, message_id=message.message_id,
                                           from_chat_id=message.chat.id)
                except:
                    await bot.send_message(chat_id=admin_id,
                                           text=f"We were unable to send your reply to the user {extractedID}")
                    pass
            else:
                await message.answer("Reply to a particular message to answer it", parse_mode="Markdown")


# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
