user_preferences = {}  # Простая реализация, для продакшена использовать базу данных

def set_language(user_id: int, language: str):
    user_preferences[user_id] = {'language': language}

def get_language(user_id: int):
    return user_preferences.get(user_id, {}).get('language', 'en')
