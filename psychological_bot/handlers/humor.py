from aiogram import types, Dispatcher
from utils.localization import get_language

async def send_joke(message: types.Message):
    lang = get_language(message.from_user.id)
    jokes = {
        'en': "Why don’t scientists trust atoms? Because they make up everything!",
        'uk': "Чому вчені не довіряють атомам? Тому що вони складають усе!",
        'ru': "Почему ученые не доверяют атомам? Потому что они составляют все!"
    }
    await message.answer(jokes[lang])

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_joke, commands='joke')
    dp.register_message_handler(send_joke, Text(equals='joke', ignore_case=True))
