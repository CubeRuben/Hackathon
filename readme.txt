1) Парсер

Директория: parcer

main.py - содержит функцую main, в которой происходит весь процесс парсинга (от загрузки отчета до вывода готовых таблиц в CSV)
parcer.py - содержит класс парсера

Для запуска парсера необходимо запусть файл main.py с помощью python

2) Модель

Директория: model

main.py - содержит функции для кластеризации и вывода изображения кластеров
converter.py - преобразует спарсенные данные в необходимые коэффициенты 

Для вывода изображения кластеров необходимо запусть файл main.py с помощью python

3) Веб-сайт

Директория: iebankclustering

Это проект на фреймворке Django

Предварительно надо загрузить базу данных по ссылке: "https://drive.google.com/file/d/1Uy6B_2H_lA_Sfet-aLlVnVZnTA_gkPSg/view?usp=sharing" (БД весит 4 Гб без архива, GitHub не одобряет)

Для запуска сервера необходимо выполнить команду "python manage.py runserver", предварительно находясь в директории проекта
Адрес сайта: "http://127.0.0.1:8000/"