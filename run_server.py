import flask
from telebot import types

from bot import *
from flask import Flask
from api_key import private_key as TOKEN
server = Flask(__name__)
FLAG = 1
APP_NAME="PersuadeMe"

@server.route('/' + TOKEN, methods=['POST'])
def get_message():
    bot.process_new_updates([types.Update.de_json(flask.request.stream.read().decode("utf-8"))])
    return "!", 200

if __name__ == "__main__":
    server.run()

