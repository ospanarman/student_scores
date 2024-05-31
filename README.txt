ОПИСАНИЕ
Приложение для управления оценками учеников. Включает в себя функциональность для создания, чтения, обновления и удаления записей о студентах и их оценках.

СТЭК:
- FastAPI
- SQLAlchemy
- SQLite



УСТАНОВКА И ЩАПУСК

1. Клонирование репозитория

git clone <URL вашего репозитория>
cd student_scores_app

2. Создание и активация виртуального окружения

python3 -m venv env
source env/bin/activate

3. Установка зависимостей

pip install -r requirements.txt

4. Запуск приложения

uvicorn main:app --reload





ИСПОЛЬЗОВАНИЕ

Перейдите по адресу http://127.0.0.1:8000/docs, отобразится документация API и будет возможность протестировать эндпоинты

Эндпоинты студентов

Создать нового студента:
POST /students/

{
    "name": "Имя студента"
}

Получить информацию о конкретном студенте:
GET /students/{student_id}

Обновить информацию о конкретном студенте:
PATCH /students/{student_id}

{
    "name": "Новое имя студента"
}

Удалить ученика:
DELETE /students/{student_id}

Эндпоинты оценок
Добавить оценку студенту:
POST /scores/

{
    "score": 95,
    "student_id": 1
}

Получить информацию о конкретной оценке:
GET /scores/{score_id}

Обновить информацию о конкретной оценке:
PATCH /scores/{score_id}

{
    "score": 98,
    "student_id": 1
}

Удалить оценку:
DELETE /scores/{score_id}





ПРИМЕР:
Создание нового студента

curl -X 'POST' \\
  'http://127.0.0.1:8000/students/' \\
  -H 'accept: application/json' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "name": "Арман Оспан"
}'

Получение информации о студенте

curl -X 'GET' \\
  'http://127.0.0.1:8000/students/1' \\
  -H 'accept: application/json'

Обновление информации о студенте

curl -X 'PATCH' \\
  'http://127.0.0.1:8000/students/1' \\
  -H 'accept: application/json' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "name": "Арман Оспан"
}'

Удаление студента

curl -X 'DELETE' \\
  'http://127.0.0.1:8000/students/1' \\
  -H 'accept: application/json'

Добавление оценки студенту

curl -X 'POST' \\
  'http://127.0.0.1:8000/scores/' \\
  -H 'accept: application/json' \\
  -H 'Content-Type: application/json' \\
  -d '{
  "score": 100,
  "student_id": 1
}'