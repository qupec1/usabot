import telebot.types
from telebot import types
import config

bot = telebot.TeleBot(config.TOKEN)


def analytics(func: callable):     #Analytics users. Who start this bot.
    def analytics_wrapper(message):

        f = open('Users.txt', 'a')
        f.write("\n")
        f.write(message.from_user.first_name)
        f.write("_user: ")
        f.write(str(message.from_user.username))
        f.close()
        return func(message)
    return analytics_wrapper

@bot.message_handler(commands=['start'])
@analytics
def start(message):
    mess = f'Хей, <b>{message.from_user.first_name}!</b> Напиши откуда ты? :)'
    mainmenu = types.InlineKeyboardMarkup()
    key1 = types.InlineKeyboardButton(text='Россия', callback_data='key1')
    mainmenu.add(key1)
    bot.send_message(message.chat.id, mess, parse_mode = 'html', reply_markup=mainmenu)
@bot.message_handler(content_types=['text'])  #Save users messages
def get_text_messages(message):
    hisc = open("messageusa.txt", "a+")
    hisc.write("\n")
    hisc.write(message.text)
    hisc.write("_user: ")
    hisc.write(str(message.from_user.username))

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == "mainmenu":
            mainmenu = types.InlineKeyboardMarkup()
            key1 = types.InlineKeyboardButton(text='Россия', callback_data='key1')
            mainmenu.add(key1)
            bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id, reply_markup=mainmenu)
    elif call.data == "key1":  # Russia
            next_menu = types.InlineKeyboardMarkup()
            key11 = types.InlineKeyboardButton(text='Политическое убежище', callback_data='key11')
            key4 = types.InlineKeyboardButton(text='Виза туриста B1/B2', callback_data='key4')
            back = types.InlineKeyboardButton(text='Назад', callback_data='mainmenu')
            next_menu.add(key11, key4, back)
            bot.edit_message_text('Выбирай путь!', call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu)
    elif call.data == "key11":  # Russia - Polit ybezhishe
            next_menu3 = types.InlineKeyboardMarkup()
            key3 = types.InlineKeyboardButton(text='Частые вопросы', callback_data='key3')
            key31 = types.InlineKeyboardButton(text='Гайд', callback_data='key31')
            back = types.InlineKeyboardButton(text='Назад', callback_data='key1')
            next_menu3.add(key3, key31, back)
            bot.edit_message_text('Подробный гайд и ответы на ваши вопросы', call.message.chat.id,
                                  call.message.message_id,
                                  reply_markup=next_menu3)
    elif call.data == "key12":  # Russia - Visa
            next_menu4 = types.InlineKeyboardMarkup()
            key4 = types.InlineKeyboardButton(text='Где получить визу сейчас', callback_data='key4')
            back = types.InlineKeyboardButton(text='Назад', callback_data='key1')
            next_menu4.add(key4,back)
            bot.edit_message_text('Подробный гайд и ответы на ваши вопросы', call.message.chat.id,
                                  call.message.message_id,
                                  reply_markup=next_menu4)
    elif call.data == "key4": #Gde poly4it visa RUS
            next_menu7 = types.InlineKeyboardMarkup()
            back = types.InlineKeyboardButton(text='Назад', callback_data='key12')
            next_menu7.add(back)
            bot.edit_message_text('<b>Где Русским получить визу США в 2022г?</b>\n'
                                  '- Казахстан.\n'
                                  '- Мальта(++)\n'
                                  '- ОАЭ(Только на Английском)\n'
                                  '- Хорватия\n'
                                  '- Австрия\n'
                                  '- Израиль.\n'
                                  'Другие страны либо маленький % одобрений для граждан СНГ либо слишком долгий срок ожиданий.\n\n'
                                  '<b>**Дети должны также получать туристическую визу США, до 14 лет возможно без посещения Собеседования.</b>\n'
                                  'Консульский сбор <b>160$</b> На каждого члена семьи.\n\n'
                                  'Если у вас есть полезная информация, пожалуйста, отправляйте нам на @usabig\n'
                                  '\n'
                                  'Если планируете получать визу США в Польше:\n'
                                  'Вам нужно будет подать документы онлайн — форму DS-160.\n'
                                  'Создать личный кабинет на сайте cgifederal.secure.force.com и заплатить визовый сбор.\n'
                                  'Поймать и записаться на открытую, удобную для вас дату собеседования.\n'
                                  'Подготовить маршрут через Европу, чтобы попасть в Польшу.(Не забудьте про Шенген)',
                                  call.message.chat.id,
                                  call.message.message_id,
                                  reply_markup=next_menu7, parse_mode="html")
    elif call.data == "key31": # Russia-Polit-Gide
            next_menu5 = types.InlineKeyboardMarkup()
            back = types.InlineKeyboardButton(text='Назад', callback_data='key11')
            next_menu5.add(back)
            bot.edit_message_text('<b>Гайд о поездке в США. Политическое Убежище</b>\n'
                                  'Путь через мексику.\n'
                                  '\n'
                                  'Краткая инструкция:\n'
                                  '<b>1.</b> Летите в Мексику.\n'
                                  '<b>2.</b> Покупаете машину в Тихуане.\n'
                                  '<b>3.</b> Пытаетесь проехать "пупырки" на границе Мексики с США.\n'
                                  '<b>4.</b> Вас арестовывают и отправляют в "бордер".\n'
                                  '<b>5.</b> Выходите из бордера и едете к своему поручителю.\n'
                                  '<b>6.</b> Встаете на учет и ждете своего интервью с офицером USCIS.\n'
                                  '<b>7.</b> Начинаете свою адаптацию в США.',
                                  call.message.chat.id,
                                  call.message.message_id,
                                  reply_markup=next_menu5, parse_mode="html")
    elif call.data == "key3": #Russia-Polit-Voprosi
            next_menu6 = types.InlineKeyboardMarkup()
            key32 = types.InlineKeyboardButton(text='Поручитель', callback_data='key32')
            key33 = types.InlineKeyboardButton(text='Документы с собой', callback_data='key33')
            back = types.InlineKeyboardButton(text='Назад', callback_data='key11')
            next_menu6.add(key32, key33, back)
            bot.edit_message_text('<b>Вопрос-Ответ:</b>\n'
                                  'Путь через мексику.\n'
                                  'Подходит вам ,если у вас НЕТ ВИЗЫ в США  и получить ее нет времени, потому что вы боитесь оставаться в своей стране.\n'
                                  'Если вы пересекаете незаконно границу Мексики с США то вы осознаете,'
                                  'что можете остаться на территории сша только запросив Политическое убежище, потому что бежите из своей страны.'
                                  '\n'
                                  '<b>Зачем через Мексику?</b>\n'
                                  '- Самый быстрый вариант попасть в США если у вас нету визы\n'
                                  '<b>Что нужно чтобы добраться до Мексики?</b>\n'
                                  '- Загранпаспорт\n'
                                  '- Электронная виза (делается на сайте)\n'
                                  '- Деньги (Чем больше тем лучше, подробнее пишите @usabig)\n'
                                  '- Кейс (Желательно сформировать структурированно свой кейс по преследованию с адвокатом до Мексики)\n'
                                  '- Наличие поручителя в США\n'
                                  '<b>Сколько денег нужно для поездки?</b>\n'
                                  '- Примерно 7,000$.\n'
                                  ' Пишите в личку, бесплатно кинем подробный разбор финансов @usabig\n'
                                  '<b>Кто может запрашивать Политическое Убежище?</b>\n'
                                  '- Тот кто подвергается преследованию (Страх смерти, Страх Тюрьмы) по нижеперечисленным категориям:\n'
                                  '- Религия (Свидетели Иеговы)\n'
                                  '- Национальность\n'
                                  '- Раса\n'
                                  '- Политическая позиция (Оппозиция и тд)\n'
                                  '- Член какой-либо социальной группы (Лгбт и тд)\n',
                                  call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu6, parse_mode="html")
    elif call.data == "key32": #politika - Pory4itel
            next_menu8 = types.InlineKeyboardMarkup()
            back = types.InlineKeyboardButton(text='Назад', callback_data='key3')
            next_menu8.add(back)
            bot.edit_message_text('<b>Зачем поручитель и где его искать?</b>\n'
                                  'Можно идти без поручителя - <b>НА СВОЙ СТРАХ И РИСК</b>.\n'
                                  '\n'
                                  '<b>Для чего нужен поручитель?</b>\n'
                                  '- Вы едите к поручителю\n'
                                  '- Офицер USCIS в бордере попросит предоставить вас адрес и телефон для связи с ПОРУЧИТЕЛЕМ\n'
                                  '- На адрес поручителя будут приходить все письма для вас от USCIS\n'
                                  '<b>Поручитель чем то рискует?</b>\n'
                                  '- НЕТ. Поручителем может быть любой человек с гринкартой или гражданин США.\n'
                                  '- Поручителю нужно ответить на звонок от USCIS, сказать, что он вас знает и что вы едете к нему.ВСЕ!\n'
                                  '<b>Обязаны ли жить у Поручителя?</b>\n'
                                  '- НЕТ. Можно жить где угодно, но первой точкой должен быть хотя бы отель рядом с адресом Поручителя.\n'
                                  '- Если решили, что едете в другой штат, то нужно по приезду уведомить местный USCIS о смене адреса.\n'
                                  '(Советуем сразу искать поручителя в штате, в котором планируете стартовать)\n'
                                  '<b>Сколько стоит Поручитель?</b>\n'
                                  '- БЕСПЛАТНО. НО! Некоторые просят за это деньги, решать вам.\n'
                                  '<b>Где найти Поручителя?</b>\n'
                                  '- Ищите в группах фейсбука в нужном вам городе "Русские в Сакраменто" "Русские в Лос Анджелесе" \n'
                                  '"Русские в Нью-Йорке" рубрики Поручитель. Или пишите сами.\n'
                                  ' Смотрите, кто уже поручался за кого нибудь в комментариях к постам.\n'
                                  '<b>Итог:</b>\n'
                                  '- Если бюджет ограничен, можно всегда найти бесплатного поручителя.\n'
                                  '- НО! Не забудьте этой человеческой доброты и поручайтесь сами,когда у вас уже будет такая возможность в США.\n'
                                  '- Также в этих группах можно в комментариях найти ответы на возникшие вопросы, по работе, аренде жилья, сады, школы и тд.\n'
                                  '- Считаю, что "помогающие организации" это последняя очередь. Редко отвечают и помогают тем, кто уже в США и не имеет другой возможности.',
                                  call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu8, parse_mode="html")
    elif call.data == "key33": # Politika-Documents
            next_menu9 = types.InlineKeyboardMarkup()
            back = types.InlineKeyboardButton(text='Назад', callback_data='key3')
            next_menu9.add(back)
            bot.edit_message_text('<b>Какие документы необходимо взять с собой?</b>\n'
                                  '<b>1.</b> Загранпаспорт на каждого члена семьи\n'
                                  '<b>2.</b> Желательно сделать по второму заграннику и отправить его поручителю перед поездкой или пусть его отправят родственники сразу после того как вы окажитесь в США\n'
                                  '<b>3.</b> Водительское удостоверение.(Если его не заберут, то можете ездить на легковом авто)\n'
                                  '<b>4.</b> Справку о несудимости(Важно!)\n'
                                  '<b>5.</b> Справку детям о прививках\n'
                                  '<b>6.</b> Табель успеваемости детей из школы',
                                  call.message.chat.id, call.message.message_id,
                                  reply_markup=next_menu9, parse_mode="html")
bot.polling(none_stop=True)