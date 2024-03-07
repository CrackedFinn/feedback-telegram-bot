from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import os
from dotenv import load_dotenv
import mysql_database

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
admin_id = os.getenv('ADMIN_ID')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # Run after /start command
async def send_welcome(message: types.Message):
    await message.answer("🛠️ *Hi!*\n\nWrite your question here and we will answer it as soon as possible.",
                         parse_mode="Markdown")


@dp.message_handler(commands=['ban'])  # Run after /ban command
async def ban_user(message: types.Message):
    if int(message.chat.id) != int(admin_id):  # USER EXPERIENCE
        await message.answer("You can't use this command", parse_mode="Markdown")
    else:  # ADMIN EXPERIENCE
        if message.reply_to_message:
            if message.reply_to_message.content_type == 'text':
                extractedID = message.reply_to_message.text.split("#")[-1]
            else:
                extractedID = message.reply_to_message.caption.split("#")[-1]
            await mysql_database.BanUser(extractedID)
            await message.answer(f"User {extractedID} was successfully banned.", parse_mode="Markdown")
        else:
            await message.answer("Reply to a particular message to answer it", parse_mode="Markdown")


@dp.message_handler(content_types=types.ContentType.all())
async def text_message(message: Message):
    supported_content_types = ['document', 'text', 'photo', 'audio', 'video', 'animation']
    if message.content_type not in supported_content_types:
        await message.answer(
            f"Sorry, your message wasn't delivered. You can't send {message.content_type} to the Support bot.",
            parse_mode="Markdown")
    else:
        if int(message.chat.id) != int(admin_id):  # USER EXPERIENCE
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


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
