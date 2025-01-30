Шаблон для создания бота на aiogram3 с БД sqlite под управлением sqlalchemy.

Создан скелет для создания бота.

Создана база данных с таблицамами и данными:

users
-id
-telegram_id
-username

categories
-id
-name

products
-id
-name
-description
-price
-category

Сделана точка запуска бота в файле main.py, первоначальный router и handler команды /start