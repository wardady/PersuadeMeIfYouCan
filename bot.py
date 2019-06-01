import telebot
from api_key import private_key
from emoji import emojize

bot = telebot.TeleBot(private_key)
man_emoji = emojize(":man:")
woman_emoji = emojize(":woman:")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    # TODO Check if user is in DB if not then add to DB and continue this branch, otherwise *new branch to be written*
    chat_id = message.chat.id
    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
    markup.add(telebot.types.KeyboardButton(man_emoji), telebot.types.KeyboardButton(woman_emoji))
    bot.send_message(chat_id, "Hi! You seem to be a new user. Let`s fill some information. Choose your sex:",
                     reply_markup=markup)


@bot.message_handler(commands=['help'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "***HELP INFORMATION TO BE PROVIDED HERE***")


@bot.message_handler(func=lambda x: x.text in [man_emoji, woman_emoji])
def process_sex(x):
    # TODO add sex to user in DB
    if x.text == man_emoji:
        print('man')
    else:
        print('woman')


@bot.message_handler(func=lambda x: True)
def echo_all(x):
    bot.reply_to(x, x.text)


bot.polling()
updates = bot.get_updates()
