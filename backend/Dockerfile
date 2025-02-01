# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /CareTrack/backend  # Указываем правильную рабочую директорию для бэкенда

# Копируем pyproject.toml и poetry.lock
COPY pyproject.toml poetry.lock ./

# Устанавливаем poetry
RUN pip install poetry

# Устанавливаем зависимости
RUN poetry install --no-interaction --no-ansi

# Копируем весь код бэкенда
COPY . .

# Открываем порт, на котором слушает ваше приложение (например, 8000)
EXPOSE 8000

# Команда для запуска приложения
CMD ["poetry", "run", "uvicorn", "main:main_app", "--host", "0.0.0.0", "--port", "8000"]