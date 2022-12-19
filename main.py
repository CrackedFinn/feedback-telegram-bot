from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import Message
import os
from dotenv import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('TOKEN'))
admin_id = os.getenv('ADMIN_ID')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])  # Run after /start command
async def send_welcome(message: types.Message):
    await message.answer("🛠️ *Hi!*\n\nWrite your question here and we will answer it as soon as possible.", parse_mode="Markdown")


@dp.message_handler(content_types=['document', 'text', 'photo', 'audio', 'video'])
async def text_message(message: Message):
    if int(message.chat.id)!=int(admin_id):
        if message.content_type == 'text':
            await bot.send_message(chat_id=admin_id, text=message.text + f"\n\n#{message.chat.id}")
        else:
            await bot.copy_message(chat_id=admin_id, message_id=message.message_id, from_chat_id=message.chat.id,
                                   caption=f"#{message.chat.id}")
    else:
        if message.reply_to_message:
            if message.reply_to_message.content_type == 'text':
                extractedID=message.reply_to_message.text.split("#")[-1]
            else:
                extractedID=message.reply_to_message.caption.split("#")[-1]
            print(extractedID)
            await bot.copy_message(chat_id=extractedID, message_id=message.message_id, from_chat_id=message.chat.id)
        else:
            await message.answer("Reply to a particular message to answer it", parse_mode="Markdown")


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=False)
