# 5743779050:AAGk_PpkbJbBy198YAI33yQ-4PsuwCzgM7Y
import telebot
from telebot import types

token ='5743779050:AAGk_PpkbJbBy198YAI33yQ-4PsuwCzgM7Y'
bot = telebot.TeleBot(token)

def create_keyboard():
    keyboart = types.ReplyKeyboardMarkup(resize_keyboard=True)
    sdacha_btn = types.InlineKeyboardButton(text="Порядок сдачи теста🤔", callback_data='1')
    doc_btn = types.InlineKeyboardButton(text="Документы для сдачи теста❓", callback_data='2')
    info_btn = types.InlineKeyboardButton(text="Информация об оплате💸", callback_data='3')
    resalt_btn = types.InlineKeyboardButton(text="Выдача рез-тов Бровки📃🏥", callback_data='4')
    vokzal_btn = types.InlineKeyboardButton(text="Выдача рез-тов Вокзал📃🚞", callback_data='5')
    aero_btn = types.InlineKeyboardButton(text="Выдача рез-тов Аэропорт📃🛩", callback_data='6')
    rezh_btn = types.InlineKeyboardButton(text="Режим работы Бровки 13🏥", callback_data='7')
    rezhv_btn = types.InlineKeyboardButton(text="Режим работы ЖД вокзал🚞", callback_data='8')
    rezha_btn = types.InlineKeyboardButton(text="Режим работы Аэропорт🛩", callback_data='9')
    dopinfo_btn = types.InlineKeyboardButton(text="Дополнительная информация📞", callback_data='10')
    keyboart.add(sdacha_btn)
    keyboart.add(doc_btn)
    keyboart.add(info_btn)
    keyboart.add(resalt_btn, vokzal_btn, aero_btn)
    keyboart.add(rezh_btn, rezhv_btn, rezha_btn)
    keyboart.add(dopinfo_btn)
    return keyboart


@bot.message_handler(commands=['start'])
def start_bot(message):
    keyboard = create_keyboard()
    bot.send_message(
        message.chat.id,
        "Вас приветствует Бот minsksanepid.by! Какую информацию Вы желаете узнать?",
        reply_markup=keyboard
    )

@bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "Порядок сдачи теста🤔"):
        bot.send_message(message.chat.id,
                         text="Прием на тестирование осуществляется по электронной записи http://reg.minsksanepid.by:8080 либо по живой очереди🚶‍️🚶🚶️")
    if (message.text == "Документы для сдачи теста❓"):
        bot.send_message(message.chat.id,
                         text="Для сдачи теста необходима ксерокопия паспорта📕 и квитанция об оплате🧾(можно в электронном виде)📱")
    if (message.text == "Информация об оплате💸"):
        img = open('plat.jpg', 'rb')
        bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption="Актуальна для всех пунктов☝")
        img.close()
    if (message.text == "Выдача рез-тов Бровки📃🏥"):
        img = open('vydaca.jpg', 'rb')
        bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption="Выдача Бровки 13")
        img.close()
    if (message.text == "Выдача рез-тов Вокзал📃🚞"):
        img = open('вокзал.jpg', 'rb')
        bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption="Выдача ЖД вокзал")
        img.close()
    if (message.text == "Выдача рез-тов Аэропорт📃🛩"):
        img = open('aero.jpg', 'rb')
        bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption="Выдача Аэропорт")
        img.close()
    if (message.text == "Режим работы Бровки 13🏥"):
        img = open('rezh brovki.jpg', 'rb')
        bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption="Режим работы Бровки 13")
        img.close()
    if (message.text == "Режим работы ЖД вокзал🚞"):
        img = open('rezh vokzal.jpg', 'rb')
        bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption="Режим работы ЖД вокзал")
        img.close()
    if (message.text == "Режим работы Аэропорт🛩"):
        img = open('zezh aeto.jpg', 'rb')
        bot.send_photo(
            chat_id=message.chat.id,
            photo=img,
            caption="Режим работы Аэропорт")
        img.close()
    if (message.text == "Дополнительная информация📞"):
        bot.send_message(message.chat.id,
                         text="Дополнительная информация по телефону 8(017)319-69-84 понедельник-пятница с 8:30 до 12:30 либо на сайте minsksanepid.by")


if __name__== "__main__":
    bot.polling(none_stop=True)


