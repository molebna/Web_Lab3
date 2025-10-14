# 1. Базовий образ Python
FROM python:3.13-slim

# 2. Робоча директорія всередині контейнера
WORKDIR /app

# 3. Копіюємо файл залежностей
COPY requirements.txt .

# 4. Встановлюємо залежності
RUN pip install --no-cache-dir -r requirements.txt

# 5. Копіюємо весь код проєкту в контейнер
COPY . .

# 6. Команда, яка виконується при запуску контейнера
CMD ["python", "bot.py"]
