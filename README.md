# Petitions API

# Установка и запуск
1. Клонируйте репозиторий:
   git clone https://github.com/abdiraiymzhandos/petitions_project.git
   cd petitions_project
2. Установите зависимости:
pip install -r requirements.txt

3. Выполните миграции:
python manage.py migrate

4. Запустите сервер разработки:
python manage.py runserver

5. Используйте команды Docker:
docker-compose up

## Тестирование API
Используйте Postman или cURL для тестирования следующих эндпоинтов:
- /api/petitions/ - CRUD для петиций
- /api/votes/ - Добавление/удаление голосов
- /api/token/ - Получение JWT токена
- /api/token/refresh/ - Обновление токена