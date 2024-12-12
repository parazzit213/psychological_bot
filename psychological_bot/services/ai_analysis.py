from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Обучение модели для анализа настроения
def train_model():
    # Пример данных для тренировки модели
    data = [
        ("I am happy", "positive"),
        ("I am sad", "negative"),
        ("I am stressed", "negative"),
        ("I am relaxed", "positive")
    ]
    
    texts, labels = zip(*data)
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(texts)
    
    model = MultinomialNB()
    model.fit(X, labels)
    
    return vectorizer, model

# Пример анализа текста
def analyze_text(text, vectorizer, model):
    X = vectorizer.transform([text])
    return model.predict(X)[0]

vectorizer, model = train_model()

# Использование модели для анализа
def analyze_user_input(user_input):
    return analyze_text(user_input, vectorizer, model)
