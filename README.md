# it-cheb
Основной стек технологий:

Python - 3.9.6;
Node.js - 14.18.0;
Vue - 4.5.15.

Среда запуска:

Проект развернут на Windows 10 64-bit;
Требуются библиотеки python;.
Требуются модули vue

Установка:

git clone https://github.com/Neto42/it-cheb.git
python -m venv venv;
cd venv\Scripts\activate;

Установка зависимостей проекта:
pip install -r requirements.txt.

Установка Fronted:
cd fronted
npm install

Создание бд:
Создаем бд в PostgressSQL, в settings.py меняем настройки бд в связи со своими данными

Применяем миграции 
python manage.py makemigrations
python manage.py migrate

Для обучения и предсказания нейронной сети использовать команды:
python manage.py educ - обучение
python manage.py pred - предсказание
