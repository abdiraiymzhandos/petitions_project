# Petitions API

# Установка и запуск
Клонируйте репозиторий:
   ```bash
   git clone <repository_url>
   cd petitions_project
Установите зависимости:
pip install -r requirements.txt

Выполните миграции:
python manage.py migrate

Запустите сервер разработки:
python3 manage.py runserver

Тестирование API
Используйте Postman или cURL для тестирования следующих эндпоинтов:
/api/petitions/ - CRUD для петиций
/api/votes/ - Добавление/удаление голосов
/api/token/ - Получение JWT токена
/api/token/refresh/ - Обновление токена