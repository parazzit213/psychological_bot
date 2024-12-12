async def send_notification(bot, user_id, message):
    await bot.send_message(user_id, message)
