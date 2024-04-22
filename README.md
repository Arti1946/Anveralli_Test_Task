#  Test task for Anveralli company

## Описание
Приложение выполнено на основе сайта kwork с минимальным функционалом.
Имеется админ-панель и личный кабинет заказчика и исполнителя.
В качестве бд выбран PostgreSQL.


## Установка

* Клонировать репозиторий командой `git clone`
* Создать виртуальное окружение командой `python -m venv venv` и активировать его командой `source venv/Scripts/activate`
* Установить зависимости командой `pip install -r requirements.txt`
* Перейти в директорию с файлом _**manage.py**_ 
* Подготовить миграции командой `python manage.py makemigrations` и запустить их `python manage.py migrate`
* Запустить приложение командой `python manage.py runserver`

## Доступные эндпоинты
### Заказы:
* Список всех заказов - [http://127.0.0.1:8000/orders/orders_list/](http://127.0.0.1:8000/orders/orders_list/)
* Подробная информация о заказе - http://127.0.0.1:8000/orders/detail/<order_id>
* Создание заказа - [http://127.0.0.1:8000/orders/order_create/](http://127.0.0.1:8000/orders/order_create/)
* Личный кабинет - просмотр заказов созданных пользователем - [http://127.0.0.1:8000/orders/lk/](http://127.0.0.1:8000/orders/lk/)

### Авторизация:
* Войти - [http://127.0.0.1:8000/auth/login/](http://127.0.0.1:8000/auth/login/)
* Регистрация - [http://127.0.0.1:8000/auth/signup/](http://127.0.0.1:8000/auth/signup/)
* Выйти - [http://127.0.0.1:8000/auth/logout/](http://127.0.0.1:8000/auth/logout/)
* Форма сброса пароля - [http://127.0.0.1:8000/auth/password_reset_form/](http://127.0.0.1:8000/auth/password_reset_form/)
* Форма смены пароля - [http://127.0.0.1:8000/auth/password_change_form/](http://127.0.0.1:8000/auth/password_change_form/)
* Просмотр профиля пользователя - [http://127.0.0.1:8000/auth/profile/<user_id>/](http://127.0.0.1:8000/auth/profile/<user_id>/)