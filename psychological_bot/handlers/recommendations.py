from aiogram import types, Dispatcher
from config import config
from utils.localization import get_language

async def send_recommendations(message: types.Message):
    lang = get_language(message.from_user.id)
    recommendations = {
        'en': "Here are some recommendations: meditation, breathing exercises, and humor.",
        'uk': "Ось деякі рекомендації: медитація, дихальні вправи та гумор.",
        'ru': "Вот некоторые рекомендации: медитация, дыхательные упражнения и юмор."
    }
    await message.answer(recommendations[lang])

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_recommendations, commands='recommendations')
    dp.register_message_handler(send_recommendations, Text(equals='recommendations', ignore_case=True))
