from aiogram import types, Dispatcher
from utils.localization import get_language

async def send_support(message: types.Message):
    lang = get_language(message.from_user.id)
    support_text = {
        'en': "If you need psychological help, please reach out to a professional.",
        'uk': "Якщо вам потрібна психологічна допомога, зверніться до професіонала.",
        'ru': "Если вам нужна психологическая помощь, обратитесь к профессионалу."
    }
    await message.answer(support_text[lang])

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_support, commands='support')
    dp.register_message_handler(send_support, Text(equals='support', ignore_case=True))
