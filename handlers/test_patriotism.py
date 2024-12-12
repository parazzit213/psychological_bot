from aiogram import types, Dispatcher
from config import config
from tests.patriotism_test import patriotism_questions
from utils.localization import get_language

async def patriotism_test(message: types.Message):
    lang = get_language(message.from_user.id)
    await message.answer(config.MESSAGES['patriotism_test_start'][lang])
    # Отправка вопросов пользователю
    for question in patriotism_questions[lang]:
        await message.answer(question)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(patriotism_test, commands='patriotism_test')
    dp.register_message_handler(patriotism_test, Text(equals='patriotism_test', ignore_case=True))
