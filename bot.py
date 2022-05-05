from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.types import CallbackQuery


Stylish=Client(
    "Stylish Bot",
    bot_token="5302212624:AAHlXG2vappLbK2gaKmD1wxJ4DJajGc6T5w",
    api_hash="5820bc246505e0ff60af5391d649f9a6",
    api_id="8406611"
)


@Stylish.on_message(filters.command("start"))
async def start_message(bot, message):
    await message.reply_text("Hi Man 😁")


Stylish.run()
