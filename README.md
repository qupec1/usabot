# Как быстро сделать TelegramBot с `inline keydoard`.
 (Данный бот помогает найти ответы на вопросы о переезде в `США`)
![preview](gifusabot.gif)

Инструкция чтобы все работало:

PS. Бота пишем на `Python`.
  1. Создаете в телеграме пустого бота с помощью бота `@BotFather`(Придумываете назваине вашего бота и получаете ключ-токен)
  2. Идете в `IDE` в которой работаете и импортируете библиотеку для работы с телеграмботами: `telebot`
  3. Создаете в папке с ботом файл `config` куда копируете `token` полученный от @BotFather.
  4. Не забываем импортировать `config`, чтобы бот запускался. 
  5. Создаем 2 файла в папке с ботом, чтобы отслеживать **кто** заходил в бота и **что** писали: `Users.txt` и `messageusa.txt`
  6. Копируем бота из [репозитория](https://github.com/qupec1/usabot.git) и все должно работать.
  7. Меняйте `меню` и `текст` как нужно для ваших проектов.
  
  
  
  
Интструкция как выгрузить бота на  **бесплатный** `сервер`:
  1. Проделываете все предыдущие шаги.
  2. Регистрируетесь на сайте [Pythonanywhere](https://www.pythonanywhere.com/)
  3. Создаете там проект(папку) с ботом. Добавляете туда 3 файла(`USAgo.py`,`messagetext.txt`,`Users.txt`)
  4. Идете там в `Bash Console`. Дублируете установленные питоновские библиотеки которые были у вас при работе с кодом.
  5. Запускаете также через эту коносль. `python USAgo.py`. 
  6. Всё! Вы сделали бота и он работает. Радуетесь! (:
  
