import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton
import config
bot = telebot.TeleBot(config.token)


def keyboard_buttons():
    markup = ReplyKeyboardMarkup()
    button1 = KeyboardButton('Гель для вмивання')
    button2 = KeyboardButton('Тонік для обличчя')
    button3 = KeyboardButton('Крем для лиця')

    markup.add(button1, button2, button3)
    return markup


def set_Inline_button():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Сухий', callback_data="dry")
    button2 = InlineKeyboardButton('Жирний', callback_data="oily")
    button3 = InlineKeyboardButton('Нормальний', callback_data="normal")

    markup.add(button1, button2, button3)
    return markup

def set_Inline_button_dry():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Cosrx', callback_data="cosrx")
    button2 = InlineKeyboardButton('Cerave', callback_data="cerave")
    button3 = InlineKeyboardButton('Dr.Jart+', callback_data="dr.jart")

    markup.add(button1, button2, button3)
    return markup

def set_Inline_button_dry1():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('The Ordinary', callback_data="ordinary")
    button2 = InlineKeyboardButton('Ziaja', callback_data="ziaja")


    markup.add(button1, button2)
    return markup

def set_Inline_button_buy_or_back():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Додати до корзини🛒', callback_data="cart")
    button2 = InlineKeyboardButton('⬅', callback_data="back")

    markup.add(button1, button2)
    return markup


def set_Inline_button_continue():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Продовжити', callback_data="continue")
    button2 = InlineKeyboardButton('Завершити', callback_data="finish")

    markup.add(button1, button2)
    return markup

def keyboard_buttons_continue():
    markup = ReplyKeyboardMarkup()
    button1 = KeyboardButton('Тонік для обличчя')
    button2 = KeyboardButton('Крем для лиця')

    markup.add(button1, button2)
    return markup

@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text:
        print(message.from_user.last_name, message.from_user.first_name)
    bot.send_message(message.chat.id, "Вітаю! Цей бот допоможе тобі скласти список косметичних засобів для догляду твого типу шкіри обличчя. Для початку вибери свій тип шкіри:",
                     reply_markup=set_Inline_button())

user_choice_keyboard = " "
@bot.message_handler(content_types=['text'])
def conversation(message):
    global user_choice_keyboard
    if message.text == "Гель для вмивання" and type_skin == "dry":
        user_choice_keyboard = "Гель для вмивання"
        bot.send_message(message.chat.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry())
    if message.text == "Тонік для обличчя" and type_skin == "dry":
        user_choice_keyboard = "Тонік для обличчя"
        bot.send_message(message.chat.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry1())

type_skin = " "
wish_list = list()
price = 0
choice = ""
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    global type_skin
    global price
    global choice
    print("hello")
    if call.data == "dry":
        type_skin = "dry"
        bot.send_message(call.from_user.id, "Оберіть певний засіб для гігієни:", reply_markup=keyboard_buttons())
        #bot.answer_callback_query(call.id, "Ось Alert-повідомлення")

    if call.data == "oily":
        type_skin = "oily"
        bot.send_message(call.from_user.id, "Оберіть певний засіб для гігієни:", reply_markup=keyboard_buttons())

    if call.data == "normal":
        type_skin = "normal"
        bot.send_message(call.from_user.id, "Оберіть певний засіб для гігієни:", reply_markup=keyboard_buttons())


    if call.data == "cosrx":
        choice = "cosrx"
        bot.send_photo(call.from_user.id, "https://cdn.notinoimg.com/detail_zoom/cosrx/8809416470511_01-o/cosrx-good-morning-cistici-gel___3.jpg")
        bot.send_message(call.from_user.id, "Cosrx – очищуючий гель для сухої шкіри. Ціна: 400 грн", reply_markup=set_Inline_button_buy_or_back())

    if call.data == "cerave":
        choice = "cerave"
        bot.send_photo(call.from_user.id, "https://cdn.notinoimg.com/detail_main_mq/cerave/3337875597180_01-o/cerave-cleansers-cistici-emulze-s-hydratacnim-ucinkem___5.jpg")
        bot.send_message(call.from_user.id, "Cerave – очищуючий гель для сухої шкіри. Ціна: 200 грн", reply_markup=set_Inline_button_buy_or_back())

    if call.data == "dr.jart":
        choice = "dr.jart"
        bot.send_photo(call.from_user.id, "https://cosibella.cz/cze_pm_Dr-Jart-Dermaclear-Micro-pH-Foam-Cistici-pena-na-oblicej-120-ml-10011_1.webp")
        bot.send_message(call.from_user.id, "Dr.Jart+ – очищуючий гель для сухої шкіри. Ціна: 600 грн", reply_markup=set_Inline_button_buy_or_back())

    if call.data == "continue" and user_choice_keyboard == "Гель для вмивання":
        bot.send_message(call.from_user.id, "Оберіть наступний засіб для гігієни:", reply_markup=keyboard_buttons_continue())

    if call.data == "back" and user_choice_keyboard == "Гель для вмивання":
        bot.send_message(call.from_user.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry())

    if call.data == "cart" and choice == "cosrx":
        price += 400
        wish_list.append("Cosrx - 300грн")
        bot.send_message(call.from_user.id, "Продовжуйте вибір або завершіть", reply_markup=set_Inline_button_continue())

    if call.data == "cart" and choice == "cerave":
        price += 200
        wish_list.append("Cerave - 200грн")
        bot.send_message(call.from_user.id, "Продовжуйте вибір або завершіть", reply_markup=set_Inline_button_continue())

    if call.data == "cart" and choice == "dr.jart":
        price += 600
        wish_list.append("Dr.Jart+ - 600грн")
        bot.send_message(call.from_user.id, "Продовжуйте вибір або завершіть", reply_markup=set_Inline_button_continue())

    if call.data == "finish":
        wish_list_end = "".join(wish_list)
        bot.send_message(call.from_user.id, f"Ось ваш вибір: {wish_list_end} \nЗагальна сума: {price}.\nДякую, що скористалися цим ботом."
                                            f" Пам'ятайте, що самолікування може бути шкідливим для вашого здоров'я, а цей бот створила людина, яка не є дерматологом чи косметологом."
                                            f" До зустрічі!")
        bot.send_photo(call.from_user.id, open("taehyung.jpg", "rb"))


bot.polling(none_stop=True)
print("Hello my name is Suzie")
print("Aaaa")
#.\venv\Scripts\activate
#Set-ExecutionPolicy Unrestricted -Scope Process