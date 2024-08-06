import telebot as tb
from telebot import types,util
import users
import workwithdb

token = "bottoken"
bot = tb.TeleBot(token)
def webAppKeyboard(): #создание клавиатуры с webapp кнопкой
   keyboard = types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True) #создаем клавиатуру
   webAppTest = types.WebAppInfo("https://calorizator.ru/analyzer/products") #создаем webappinfo - формат хранения url
   one_butt = types.KeyboardButton(text="Тест WebAPP", web_app=webAppTest) #создаем кнопку типа webapp
   keyboard.add(one_butt) #добавляем кнопки в клавиатуру

   return keyboard #возвращаем клавиатуру

@bot.message_handler(commands=['start'],chat_types='private')
def start_cmd(message):
    if workwithdb.find_userinfo(message.from_user.username,1) == "":
        bot.send_message(message.chat.id,'Привет! Я — чат-бот здорового питания.\nЯ помогу тебе составить план питания, который подойдёт именно тебе.\nВведи свое имя:')
        bot.register_next_step_handler(message, namegetter)
    else:
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton("Новый прием пищи",callback_data='priem')
        btn2 = types.InlineKeyboardButton("Что я ел?",callback_data='whatieat')
        btn3 = types.InlineKeyboardButton("Инфо",callback_data='info')
        btn4 = types.InlineKeyboardButton("Информация о профиле",callback_data='profile')
        kb.row(btn1)
        kb.row(btn2,btn3)
        kb.row(btn4)
        bot.send_message(message.chat.id,'Это меню. Тут вы можете управлять вашим питанием.',reply_markup=kb)




@bot.callback_query_handler(func= lambda callback:callback.data == "priem")
def priem_pishi(callback):
    bot.send_message(callback.message.chat.id, 'Погнали!', reply_markup=webAppKeyboard())
    #   keybord = types.InlineKeyboardMarkup(row_width=3)
  #  btn1 = types.InlineKeyboardButton('Мясо',callback_data='meat')
   # btn2 = types.InlineKeyboardButton('Овощи',callback_data='veget')
    #btn3 = types.InlineKeyboardButton('Фрукты',callback_data='fruts')
    #btn4 = types.InlineKeyboardButton('Рыба',callback_data='fish')
    #btn5 = types.InlineKeyboardButton("Орехи",callback_data='orechs')
    #btn6 = types.InlineKeyboardButton("Сладости/Мучное",callback_data='sweets')
    #btn7 = types.InlineKeyboardButton("Гарнир",callback_data='dishmain')
    #keybord.row(btn1,btn2,btn3)
    #keybord.row(btn4,btn5,btn7)
    #keybord.row(btn6)

   # bot.send_message(callback.message.chat.id,"Выберите категорию:",reply_markup=keybord)


#@bot.callback_query_handler(func= lambda x:x.data in ['meat','veget','fruts','fish','orechs','sweets','dishmain'])
#def getfood(callback):
    #users.dish = callback.data
    #bot.register_next_step_handler(callback.message,kkal)
#def kkal(message):
    #print(message.text,users.dish)





@bot.message_handler(commands=['premium'],chat_types='private')
def ispremium(message):
    bot.send_message(message.chat.id,"<i>Премиум-режим в разработке! Наслаждайтесь.</i>",parse_mode="HTML")


@bot.message_handler(commands=['lk'],chat_types='private')
def showprofile(message):

    bot.send_message(message.chat.id,f'Ваша информация:\n{workwithdb.find_userinfo(message.from_user.username,1)} - Псвдоним.\n{workwithdb.find_userinfo(message.from_user.username,2)} - Ваше имя.\n{workwithdb.find_userinfo(message.from_user.username,3)} - Ваш рост.\n{workwithdb.find_userinfo(message.from_user.username,4)} - Ваш вес.\n<b>Подписка Premium - Не Активна</b> ',parse_mode="HTML")


@bot.callback_query_handler(func= lambda callback:callback.data == "profile")
def showprofile(callback):

    bot.send_message(callback.message.chat.id,f'Ваша информация:\n{workwithdb.find_userinfo(callback.from_user.username,1)} - Псвдоним.\n{workwithdb.find_userinfo(callback.from_user.username,2)} - Ваше имя.\n{workwithdb.find_userinfo(callback.from_user.username,3)} - Ваш рост.\n{workwithdb.find_userinfo(callback.from_user.username,4)} - Ваш вес.\n<b>Подписка Premium - Не Активна</b> ',parse_mode="HTML")


@bot.callback_query_handler(func = lambda callback:callback.data =="info")
def infocb(callback):
    bot.send_message(callback.message.chat.id,"🔘 Случайный совет: 🔘")
    sovet = users.get_sovet()
    bot.send_message(callback.message.chat.id,sovet)


@bot.callback_query_handler(func= lambda callback:callback.data)
def yesd(callback):
    if 'yesn' in callback.data:
        callback1=callback.data.split()
        users.name = callback1[1]
        print(users.name)
        bot.send_message(callback.message.chat.id,'Введите свой рост:')
        bot.register_next_step_handler(callback.message,rost)
    if callback.data =="non":
        bot.send_message(callback.message.chat.id, "Введите новое имя")
        bot.register_next_step_handler(callback.message, namegetter)
def namegetter(message):
    kb = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton('Да',callback_data=f'yesn {message.text}')
    btn2=types.InlineKeyboardButton(text='Нет',callback_data='non')
    kb.add(btn1)
    kb.add(btn2)
    bot.send_message(message.chat.id,f"Ваше имя - {message.text}, верно?",reply_markup=kb)
def rost(message):
    users.rost = message.text
    print(users.rost)
    bot.reply_to(message,'Введите ваш вес:')
    bot.register_next_step_handler(message,ves)
def ves(message):
    users.weight = message.text
    print(users.weight)
    keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn = types.KeyboardButton('Продолжить')
    keyb.add(btn)
    workwithdb.newuser(message.from_user.username,users.name,users.rost,users.weight)
    bot.reply_to(message,"Отличные новости! Мы успешно собрали всю необходимую информацию. Теперь мы можем приступить к следующему этапу!")
    bot.send_message(message.chat.id,f'Ваша информация:{message.from_user.username} - Псвдоним.\n{users.name} - Ваше имя.\n {users.rost} - Ваш рост.\n{users.weight} - Ваш вес.',reply_markup=keyb)


@bot.message_handler(content_types=['text'],func= lambda x:x.text=="Продолжить")
def onnext(msg):
    if users.name != "":
        bot.send_message(msg.chat.id,'Полезные советы')
        newtext= util.smart_split(users.text,500)
        keyb = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn = types.KeyboardButton('/start')
        keyb.add(btn)
        for i in newtext:
            bot.send_message(msg.chat.id, i,reply_markup=keyb)

bot.infinity_polling()