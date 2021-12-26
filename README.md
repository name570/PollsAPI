# Запуск сервера
Для старта сервера, необходимо перейти в директорию проекта и запустить файл
*runserver.bat*

#Администрирование
Для добавления/изменения/удаления опросов и вопросов необходимо создать пользователя для доступа
в админ-панель
<br/>
*python manage.py createsuperuser*
<br/>

#API
###Получение списка активных вопросов
#### url: http://127.0.0.1:8000/api/active_polls/
Архитектурный стиль - REST
<br/>
Метод - GET

Пример ответа:
<br/>
```javascript
{
    "polls": [
        {
            "poll_name": "Опрос 1",
            "poll_description": "Опрос о ворослях"
        },
        {
            "poll_name": "Опрос 3",
            "poll_description": "Опрос о креветках"
        }
    ]
}
```

###Получение детализированного списка ответа пользователя
#### url: http://127.0.0.1:8000/api/detailed_polls
Архитектурный стиль - REST
<br/>
Метод - GET
<br/>
Query parameters:
* user_id - уникальный идентификатор пользователя

<br/>
Пример запроса:
<br/>
http://127.0.0.1:8000/api/detailed_polls?user_id=45353453

Пример ответа:
<br/>
```javascript
{
    "detailed_polls": [
        {
            "answer_text": "Да",
            "question_id": {
                "question_text": "Водоросли?",
                "poll_relation": {
                    "poll_name": "Опрос 1",
                    "poll_description": "Опрос о ворослях"
                }
            }
        },
        {
            "answer_text": "Нет",
            "question_id": {
                "question_text": "Синие водоросли?",
                "poll_relation": {
                    "poll_name": "Опрос 1",
                    "poll_description": "Опрос о ворослях"
                }
            }
        },
        {
            "answer_text": "Нет",
            "question_id": {
                "question_text": "Креветки?",
                "poll_relation": {
                    "poll_name": "Опрос 3",
                    "poll_description": "Опрос о креветках"
                }
            }
        }
    ]
}
```
###Добавление ответа пользователя
#### url: http://127.0.0.1:8000/api/detailed_polls
Архитектурный стиль - REST
<br/>
Метод - POST
<br/>
#####Описание body

1. user_id - уникальный идентификатор пользователя. <br/>При отсутствии считается, что
на вопросы отвечали анонимно.
2. answers - список ответов состоящий из:
   1. answer_text - ответ пользователя
   2. question_id - уникальный идентификатор вопроса.<br/> При отсуствии в системе
вопроса с данным идентификатором считается, что запрос невалиден.

<br/>
Пример запроса валидного запроса:
<br/>
http://127.0.0.1:8000/api/detailed_polls

body:
<br/>
```javascript
{
   "user_id":"1111",
   "answers":[
      {
         "answer_text":"Да",
         "question_id":"2"
      },
      {
         "answer_text":"Нет",
         "question_id":"1"
      }
   ]
}
```
Пример ответа:
<br/>
HTTP 200 OK <br/>
Allow: GET, POST, HEAD, OPTIONS <br/>
Content-Type: application/json <br/>
Vary: Accept <br/>

Пример невалидного запроса:
<br/>
http://127.0.0.1:8000/api/detailed_polls

body:
<br/>
```javascript
{
   "user_id":"1111",
   "answers1":[
      {
         "answer_text":"Да",
         "question_id":"2"
      },
      {
         "answer_text":"Нет",
         "question_id":"1"
      }
   ]
}
```

Пример ответа:<br/>
HTTP 400 Bad Request<br/>
Allow: GET, POST, HEAD, OPTIONS<br/>
Content-Type: application/json<br/>
Vary: Accept<br/>

##Функционал пользователя
У пользователя имеется возможность:
1. Посмотреть список активных опросов
2. Пройти активный опрос
3. Посмотреть пройденные им опросы по своему уникальному идентификатору. <br/>
Просмотр анонимных ответов не предусмотрен.
4. Просмотреть детализированные ответы на пройденные им опросы.