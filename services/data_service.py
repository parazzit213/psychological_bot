user_data = {}  # В реальном приложении данные должны храниться в базе данных

def save_user_data(user_id, data):
    user_data[user_id] = data

def get_user_data(user_id):
    return user_data.get(user_id, {})
