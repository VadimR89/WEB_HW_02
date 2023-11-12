# Використовуємо офіційний образ Python
FROM python:3.11

# Робочий каталог в контейнері
WORKDIR /app

# Копіюємо файли проекту в контейнер
COPY . /app

# Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# Вказуємо команду для запуску додатка при старті контейнера
CMD ["python", "__main__.py"]