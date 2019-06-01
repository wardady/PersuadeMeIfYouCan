import telebot
from api_key import private_key
from emoji import emojize

bot = telebot.TeleBot(private_key)
man_emoji = emojize(":man:")
woman_emoji = emojize(":woman:")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    print(message)
    # TODO Check if user is in DB if not then add to DB and continue this branch, otherwise *new branch to be written*
    chat_id = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    markup.add(telebot.types.KeyboardButton(man_emoji), telebot.types.KeyboardButton(woman_emoji))
    new_msg = bot.send_message(chat_id, "Hi! You seem to be a new user. Let`s fill some information. Choose your sex:",
                               reply_markup=markup)
    bot.register_next_step_handler(new_msg, process_sex)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "***HELP INFORMATION TO BE PROVIDED HERE***")


def process_sex(x):
    chat_id = x.chat.id
    markup = telebot.types.ReplyKeyboardMarkup()
    if x.text in (man_emoji, woman_emoji):
        # TODO add sex to user in DB
        markup = telebot.types.ReplyKeyboardRemove(selective=False)
        new_msg = bot.send_message(chat_id,
                                   "Thanks, now tell me your age (please input only number):",
                                   reply_markup=markup)
        bot.register_next_step_handler(new_msg, process_age)
        print('Sex_registered')
    else:
        new_msg = bot.send_message(chat_id, "Ooops... Wrong input, please, choose from the options below.")
        bot.register_next_step_handler(new_msg, process_sex)


def process_age(message):
    chat_id = message.chat.id
    if str.isalnum(message.text):
        # TODO add age to DB
        age = int(message.text)
        print(age)
        pass
    else:
        new_msg = bot.send_message(chat_id, "Please, input only number:")
        bot.register_next_step_handler(new_msg, process_age)


@bot.message_handler(func=lambda x: True)
def echo_all(x):
    bot.reply_to(x, x.text)


bot.polling()
updates = bot.get_updates()
