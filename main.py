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


    markup.add(button1)
    return markup

def set_Inline_button_dry_gel():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Cosrx', callback_data="cosrx")
    button2 = InlineKeyboardButton('Cerave', callback_data="cerave")
    button3 = InlineKeyboardButton('Dr.Jart+', callback_data="dr.jart")

    markup.add(button1, button2, button3)
    return markup

def set_Inline_button_dry_toner():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Pyunkang Yul', callback_data="yul")
    button2 = InlineKeyboardButton('Jung Relief Toner', callback_data="jung")

    markup.add(button1, button2)
    return markup

def set_Inline_button_dry_cream():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('La Roche-Posay ', callback_data="roche-posay")
    button2 = InlineKeyboardButton('CeraVe', callback_data="cerave_cream")

    markup.add(button1, button2, )
    return markup

def set_Inline_button_buy_or_back():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Додати до корзини🛒', callback_data="cart")
    button2 = InlineKeyboardButton('⬅', callback_data="back")

    markup.add(button1, button2)
    return markup

def set_Inline_button_buy_or_back_toner():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Додати до корзини🛒', callback_data="cart_toner")
    button2 = InlineKeyboardButton('⬅', callback_data="back")

    markup.add(button1, button2)
    return markup

def set_Inline_button_buy_or_back_cream():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Додати до корзини🛒', callback_data="cart_cream")
    button2 = InlineKeyboardButton('⬅', callback_data="back")

    markup.add(button1, button2)
    return markup

def set_Inline_button_continue():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Продовжити', callback_data="continue")
    button2 = InlineKeyboardButton('Завершити', callback_data="finish")

    markup.add(button1, button2)
    return markup

def set_Inline_button_finish():
    markup = InlineKeyboardMarkup()
    button1 = InlineKeyboardButton('Завершити', callback_data="finish")

    markup.add(button1)
    return markup


def keyboard_buttons_continue():
    markup = ReplyKeyboardMarkup()
    button1 = KeyboardButton('Тонік для обличчя')
    button2 = KeyboardButton('Крем для лиця')

    markup.add(button1, button2)
    return markup

def keyboard_buttons_continue1():
    markup = ReplyKeyboardMarkup()
    button1 = KeyboardButton('Крем для лиця')

    markup.add(button1)
    return markup


@bot.message_handler(commands=['start'])
def send_welcome(message):
    if message.text:
        print(message.from_user.last_name, message.from_user.first_name)
    bot.send_message(message.chat.id, "Вітаю! Цей бот допоможе тобі скласти список косметичних засобів для догляду cухої шкіри обличчя. Для початку вибери свій тип шкіри:",
                     reply_markup=set_Inline_button())

@bot.message_handler(commands=['where_to_buy'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Cosrx - https://makeup.com.ua/ua/product/314143/ \nCeraVe - https://makeup.com.ua/ua/product/729293/7"
                                      "\nDr.Jart+ - https://makeup.com.ua/ua/product/597763/ \nPyunkang Yul -  https://makeup.com.ua/ua/product/610947/ "
                                      "\nSoon Jung PH 5.5 Relief Toner - https://rozetka.com.ua/306077468/p306077468/ "
                                      "\nLa Roche-Posay Nutritic Intense Riche - https://makeup.com.ua/ua/product/65079/ "
                                      "\nCeraVe Moisturizing Cream - https://makeup.com.ua/ua/product/729955/")


@bot.message_handler(commands=['about_me'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Привіт! Мене звати Іванка, мені 15 років. Саме я створила цей телеграм-бот. "
                                      "Навчаюся в go_iteens вже пів року. Саме завдяки моїм викладачам я змогла написати бота)")

user_choice_keyboard = " "

@bot.message_handler(content_types=['text'])
def conversation(message):
    global user_choice_keyboard
    if message.text == "Гель для вмивання" and type_skin == "dry":
        user_choice_keyboard = "Гель для вмивання"
        bot.send_message(message.chat.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry_gel())
    if message.text == "Тонік для обличчя" and type_skin == "dry":
        user_choice_keyboard = "Тонік для обличчя"
        bot.send_message(message.chat.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry_toner())
    if message.text == "Крем для лиця" and type_skin == "dry":
        user_choice_keyboard = "Крем для лиця"
        bot.send_message(message.chat.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry_cream())

type_skin = " "
wish_list = list()
price = 0
choice = ""
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == "dry":
        global type_skin
        type_skin = "dry"
        bot.send_message(call.from_user.id, "Оберіть певний засіб для гігієни:", reply_markup=keyboard_buttons())
        #bot.answer_callback_query(call.id, "Ось Alert-повідомлення")


    def gel_dry():
        global choice
        if call.data == "cosrx":
            choice = "cosrx"
            bot.send_photo(call.from_user.id, "https://cdn.notinoimg.com/detail_zoom/cosrx/8809416470511_01-o/cosrx-good-morning-cistici-gel___3.jpg")
            bot.send_message(call.from_user.id, "Cosrx – очищуючий гель для сухої шкіри. Ціна: 420 грн - 150мл", reply_markup=set_Inline_button_buy_or_back())

        if call.data == "cerave":
            choice = "cerave"
            bot.send_photo(call.from_user.id, "https://cdn.notinoimg.com/detail_main_mq/cerave/3337875597180_01-o/cerave-cleansers-cistici-emulze-s-hydratacnim-ucinkem___5.jpg")
            bot.send_message(call.from_user.id, "Cerave – очищуючий гель для сухої шкіри. Ціна: 291 грн", reply_markup=set_Inline_button_buy_or_back())

        if call.data == "dr.jart":
            choice = "dr.jart"
            bot.send_photo(call.from_user.id, "https://cosibella.cz/cze_pm_Dr-Jart-Dermaclear-Micro-pH-Foam-Cistici-pena-na-oblicej-120-ml-10011_1.webp")
            bot.send_message(call.from_user.id, "Dr.Jart+ – очищуючий гель для сухої шкіри. Ціна: 600 грн", reply_markup=set_Inline_button_buy_or_back())
    gel_dry()

    def toner_dry():
        global choice
        if call.data == "yul":
            choice = "yul"
            bot.send_photo(call.from_user.id,"https://m.media-amazon.com/images/I/512OSb20-GL._AC_UF1000,1000_QL80_.jpg")
            bot.send_message(call.from_user.id, "Корейський бренд натуральної косметики Pyunkang Yul - Essence Toner для чудового поглинання та інтенсивного зволоження сухої шкіри лиця."
                                                " Ціна: 413 грн - 100мл", reply_markup=set_Inline_button_buy_or_back_toner())
        if call.data == "jung":
            choice == "jung"
            bot.send_photo(call.from_user.id,
                           "https://img.joomcdn.net/76e03c33177b696074d0c9431f8ff54b97101bd8_original.jpeg")
            bot.send_message(call.from_user.id, "Soon Jung PH 5.5 Relief Toner - тонік, що зволожує, пом'якшує та відновлює суху шкіру обличчя. "
                                                "Ціна: 397 грн - 80мл", reply_markup=set_Inline_button_buy_or_back_toner())
    toner_dry()

    def cream_dry():
        global choice
        if call.data == 'roche-posay':
            choice = "roche-posay"
            bot.send_photo(call.from_user.id,
                           "https://img.the-village.com.ua/the-village.com.ua/post_image-image/9CUiF2O73cmKicSlxoDtrw.jpg")
            bot.send_message(call.from_user.id, "Живильний крем Nutritic Intense Riche живить і зволожує cуху шкіру лиця, "
                                                "а також відновлює її бар’єрну функцію. Ціна: 687 грн - 50мл", reply_markup=set_Inline_button_buy_or_back_cream())
        if call.data == "cerave_cream":
            choice = "cerave_cream"
            bot.send_photo(call.from_user.id,
                           "https://img.the-village.com.ua/the-village.com.ua/post_image-image/P2IiTauGABKgxKgkM79ipA.jpg")
            bot.send_message(call.from_user.id, "Зволожувальний крем для сухої та дуже сухої шкіри обличчя й тіла CeraVe Moisturizing Cream "
                                                "відновлює природний бар’єр шкіри, а також містить гіалуронову кислоту. Ціна: 482 грн - 340мл",
                             reply_markup=set_Inline_button_buy_or_back_cream())
    cream_dry()

    def add_func():
        if call.data == "continue" and user_choice_keyboard == "Гель для вмивання":
            bot.send_message(call.from_user.id, "Оберіть наступний засіб для гігієни:", reply_markup=keyboard_buttons_continue())

        if call.data == "back" and user_choice_keyboard == "Гель для вмивання":
            bot.send_message(call.from_user.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry_gel())

        if call.data == "continue" and user_choice_keyboard == "Тонік для обличчя":
            bot.send_message(call.from_user.id, "Оберіть наступний засіб для гігієни:", reply_markup=keyboard_buttons_continue1())

        if call.data == "back" and user_choice_keyboard == "Тонік для обличчя":
            bot.send_message(call.from_user.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry_toner())

        if call.data == "back" and user_choice_keyboard == "Крем для лиця":
            bot.send_message(call.from_user.id, "Оберіть бажаний продукт:", reply_markup=set_Inline_button_dry_cream())
    add_func()

    def cart_gel():
        global price
        if call.data == "cart" and choice == "cosrx":
            price += 420
            wish_list.append("Cosrx - 300грн")
            bot.send_message(call.from_user.id, "Продовжуйте вибір або завершіть", reply_markup=set_Inline_button_continue())

        if call.data == "cart" and choice == "cerave":
            price += 291
            wish_list.append("Cerave - 200грн")
            bot.send_message(call.from_user.id, "Продовжуйте вибір або завершіть", reply_markup=set_Inline_button_continue())

        if call.data == "cart" and choice == "dr.jart":
            price += 600
            wish_list.append("Dr.Jart+ - 600грн")
            bot.send_message(call.from_user.id, "Продовжуйте вибір або завершіть", reply_markup=set_Inline_button_continue())

    cart_gel()

    def cart_toner():
        global price
        if call.data == "cart_toner" and choice == "yul":
            price += 413
            wish_list.append("Pyunkang Yul - 413грн")
            bot.send_message(call.from_user.id, "Продовжуйте вибір або завершіть", reply_markup=set_Inline_button_continue())

        if call.data == "cart_toner" and choice == "jung":
            price += 397
            wish_list.append("Soon Jung - 397грн")
            bot.send_message(call.from_user.id, "Продовжуйте вибір або завершіть", reply_markup=set_Inline_button_continue())

    cart_toner()

    def cart_cream():
        global price
        if call.data == "cart_cream" and choice == "roche-posay":
            price += 687
            wish_list.append("La Roche-Posay - 687грн")
            bot.send_message(call.from_user.id, "Завершити", reply_markup=set_Inline_button_finish())

        if call.data == "cart_cream" and choice == "cerave_cream":
            price += 482
            wish_list.append("CeraVe Cream - 482грн")
            bot.send_message(call.from_user.id, "Завершити",
                             reply_markup=set_Inline_button_finish())
        print(wish_list)

    cart_cream()


    if call.data == "finish":
        wish_list_end = ", ".join(wish_list)
        bot.send_message(call.from_user.id, f"Ось ваш вибір: {wish_list_end} \nЗагальна сума: {price}.\nДякую, що скористалися цим ботом."
                                            f" Пам'ятайте, що самолікування може бути шкідливим для вашого здоров'я, а цей бот створила людина, "
                                            f"яка не є дерматологом чи косметологом."
                                            f" До зустрічі!")
        bot.send_photo(call.from_user.id, open("taehyung.png", "rb"))


bot.polling(none_stop=True)