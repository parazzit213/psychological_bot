from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.i18n import I18nMiddleware
from aiogram.utils import executor
from config import config
from handlers import start, test_stress, test_patriotism, recommendations, humor, support, feedback
import logging

# Установим уровень логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

# Настройка локализации
i18n = I18nMiddleware('bot', config.LANGUAGES, default=config.DEFAULT_LANGUAGE)
dp.middleware.setup(i18n)

# Регистрация хендлеров
start.register_handlers(dp)
test_stress.register_handlers(dp)
test_patriotism.register_handlers(dp)
recommendations.register_handlers(dp)
humor.register_handlers(dp)
support.register_handlers(dp)
feedback.register_handlers(dp)

# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
