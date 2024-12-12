from aiogram import types, Dispatcher
from utils.localization import get_language
from services.data_service import save_user_data, get_user_data

async def ask_mood(message: types.Message):
    lang = get_language(message.from_user.id)
    feedback_texts = {
        'en': "How are you feeling today?",
        'uk': "Як ви сьогодні почуваєтеся?",
        'ru': "Как вы себя чувствуете сегодня?"
    }
    await message.answer(feedback_texts[lang])

async def receive_mood_response(message: types.Message):
    mood = message.text
    user_id = message.from_user.id
    user_data = get_user_data(user_id)
