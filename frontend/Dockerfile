   # Используем базовый образ node.js
   FROM node:18-slim

   # Устанавливаем рабочую директорию
   WORKDIR /app/frontend

   # Копируем package.json и package-lock.json
   COPY package*.json ./

   # Устанавливаем зависимости
   RUN npm install

   # Копируем весь код фронтенда
   COPY . .

   # Открываем порт, на котором слушает ваше приложение (например, 3000)
   EXPOSE 3000

   # Команда для запуска приложения
   CMD ["npm", "start"]
