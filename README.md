# Проект c Django Workshop
## Записи 

* [Часть 1](https://www.youtube.com/watch?v=G-7T5Z5lQ84&feature=youtu.be)
* Часть 2

## Запуск проекта 

Проект использует `PostgreSQL` в качестве базы данных.

* https://info-comp.ru/sisadminst/684-install-postgresql-11-on-windows.html — инструкция для установки на Windows
* https://www.digitalocean.com/community/tutorials/postgresql-ubuntu-16-04-ru — инструкция для установки на Ubuntu

Для запуска приложения потребуется установить пакет `pipenv`. После установки в папке с `Pipfile` нужно выполнить команду `pipenv install`. Эта команда установит все необходимые зависимости и запустит виртуальное окружение. Внутри виртуального окружения нужно перейти в папку с файлом `manage.py` и сначала накатить миграции с помощью `python manage.py migrate`, а затем уже можно запустить тестовый сервер с помощью `python manage.py runserver 8000`.
