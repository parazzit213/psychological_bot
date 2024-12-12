from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from config import config
from utils.localization import set_language, get_language

async def cmd_start(message: types.Message):
    lang = get_language(message.from_user.id) or config.DEFAULT_LANGUAGE
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [types.KeyboardButton(text) for text in ["Tests", "Recommendations", "Humor", "Support"]]
    keyboard.add(*buttons)
    await message.answer(config.MESSAGES['start'][lang], reply_markup=keyboard)

async def set_language_handler(message: types.Message):
    lang = message.text.lower()
    if lang in config.LANGUAGES:
        set_language(message.from_user.id, lang)
        await message.answer(config.MESSAGES['start'][lang])
    else:
        await message.answer("Invalid language selected.")

async def handle_menu(message: types.Message):
    if message.text == 'Tests':
        await message.answer("Select a test:\n- Stress Test\n- Patriotism Test")
    elif message.text == 'Recommendations':
        await message.answer("Here are some recommendations: meditation, breathing exercises, and humor.")
    elif message.text == 'Humor':
        await send_joke(message)
    elif message.text == 'Support':
        await send_support(message)

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands='start')
    dp.register_message_handler(set_language_handler, Text(equals=['en', 'uk', 'ru'], ignore_case=True))
    dp.register_message_handler(handle_menu, Text(equals=['Tests', 'Recommendations', 'Humor', 'Support'], ignore_case=True))
