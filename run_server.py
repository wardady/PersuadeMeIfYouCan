import flask
from bot import bot
from telebot import types
import os
from api_key import private_key as TOKEN

server = flask.Flask(__name__)
bot.remove_webhook()


@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates(
        [types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    bot.set_webhook(
        url="https://{}.herokuapp.com/{}".format('persmeifyoucan', TOKEN))
    return "Hello from Heroku!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
