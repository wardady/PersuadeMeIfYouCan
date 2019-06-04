import flask
from telebot import types
import os

from bot import *
from api_key import private_key
from flask import Flask

server = Flask(__name__)
FLAG = 1
APP_NAME = "persuademeifyoucan"



@server.route('/' + private_key, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route('/', methods=["GET"])
def index():
    bot.remove_webhook()
    bot.set_webhook(url="https://{}.herokuapp.com/{}".format(APP_NAME, private_key))
    return "Hello from Heroku!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))


