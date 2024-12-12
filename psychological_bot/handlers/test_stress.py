from aiogram import types, Dispatcher
from config import config
from tests.stress_test import stress_questions
from utils.localization import get_language

async def stress_test(message: types.Message):
    lang = get_language(message.from_user.id)
    await message.answer(config.MESSAGES['stress_test_start'][lang])
    # Отправка вопросов пользователю
    for question in stress_questions[lang]:
        await message.answer(question)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(stress_test, commands='stress_test')
    dp.register_message_handler(stress_test, Text(equals='stress_test', ignore_case=True))
