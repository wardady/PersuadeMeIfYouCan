import telebot
import random
from api_key import private_key
from emoji import emojize
from message import temp_msg

bot = telebot.TeleBot(private_key)
man_emoji = emojize(":man:")
woman_emoji = emojize(":woman:")


# noinspection PyUnreachableCode
@bot.message_handler(commands=['start'])
def send_welcome(message):
    # TODO Check if user is in DB if not then add to DB and continue this branch, otherwise *new branch to be written*
    chat_id = message.chat.id
    if 1:  # TODO if registered
        markup = telebot.types.ReplyKeyboardMarkup(row_width=2)
        markup.add(telebot.types.KeyboardButton(man_emoji), telebot.types.KeyboardButton(woman_emoji))
        new_msg = bot.send_message(chat_id,
                                   "Hi! You seem to be a new user. Let`s fill some information. Choose your sex:",
                                   reply_markup=markup)
        bot.register_next_step_handler(new_msg, process_sex)
    else:  # TODO select all topics from DB
        new_msg = bot.send_message(chat_id, "Hello, let`s make some conversations!")
        choose_topic(message)


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
    else:
        new_msg = bot.send_message(chat_id, "Ooops... Wrong input, please, choose from the options below.")
        bot.register_next_step_handler(new_msg, process_sex)


def process_age(message):
    chat_id = message.chat.id
    if str.isalnum(message.text) and 0 < int(message.text) < 100:
        # TODO add age to DB
        age = int(message.text)
        new_msg = bot.send_message(chat_id,
                                   "Registration complete, now we can proceed to conversations!")
        choose_topic(message)
    else:
        new_msg = bot.send_message(chat_id, "Please, input only number:")
        bot.register_next_step_handler(new_msg, process_age)


@bot.message_handler(commands=['topic'])
def choose_topic(message):
    chat_id = message.chat.id
    # TODO select all topics from DB
    topics = ['sport', 'politics', 'religion', 'games', 'gender equality', 'very interesting topc', 'one more',
              'for test', 'pls', 'want', 'to', 'die', 'stop']
    markup = telebot.types.ReplyKeyboardMarkup()
    for topic in topics:
        markup.add(telebot.types.KeyboardButton(topic))
    new_msg = bot.send_message(chat_id,
                               "Chose the topic:", reply_markup=markup)
    bot.register_next_step_handler(new_msg, __chosen_topic)


def __chosen_topic(msg):
    chat_id = msg.chat.id
    markup = telebot.types.ReplyKeyboardRemove(selective=False)
    bot.send_message(chat_id, "You choose " + msg.text, reply_markup=markup)
    question_generator(msg)


def question_generator(message):
    chat_id = message.chat.id
    topic = message.text
    # TODO Select all questions with this topic !IMPORTANT CHECK IF NO SUCH QUESTIONS
    questions = ['kek', 'lol']
    if questions:
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(telebot.types.InlineKeyboardButton(emojize(":thumbs_up:"), callback_data='yes ' + topic),
                   telebot.types.InlineKeyboardButton(emojize(":thumbs_down:"), callback_data='no ' + topic),
                   telebot.types.InlineKeyboardButton(emojize(":left-right_arrow:"), callback_data='skip ' + topic))
        bot.send_message(chat_id, random.choice(questions), reply_markup=markup)
    else:
        bot.send_message(chat_id,
                         "Sorry, no questions in this topic. Try another:")
        choose_topic(message)


@bot.callback_query_handler(lambda q: q.message.chat.type == "private")
def private_query(query):
    reply, topic = query.data.split()
    bot.edit_message_reply_markup(query.message.chat.id, query.message.message_id)
    if reply == 'skip':
        msg = temp_msg(chat_id=query.message.chat.id, text=topic)
        question_generator(msg)
    # TODO GET CONVERSATION IF NEEDED ELSE, POST ANSWER TO DB, CONTINUE AS IN SKIP
    elif reply == 'yes':
        pass
    elif reply == 'no':
        pass


@bot.message_handler(func=lambda x: True)
def echo_all(x):
    bot.reply_to(x, "Sorry, not supported action " + x.text)


bot.polling()
updates = bot.get_updates()
