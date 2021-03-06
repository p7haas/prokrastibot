# -*- coding: utf-8 -*-
""" A simple group.me chat bot.
"""
from flask import Flask, request
import groupme
import brain


app = Flask(__name__)
app.debug = True


# @app.route('/')
# def hello():
#     app.logger.debug("default route hit")
#     return 'nok'


@app.route('/ping', methods=['GET', 'POST'])
def ping():
    """ Process and respond to a group.me callback.
    """
    message = groupme.BotCallback(request.get_json(force=True))
    app.logger.debug("/ping received this: {}".format(str(message)))

    answers = [groupme.BotMessage(x) for x in brain.answer(message)]

    for answer in answers:
        app.logger.debug("/ping will send that: {}".format(answer))
        groupme.bot_send(answer)

    return 'ok'
