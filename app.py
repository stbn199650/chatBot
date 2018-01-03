import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

API_TOKEN = '477187378:AAGb_zxY7MSrd3AKwnNsS-YDZpC95z9oRmE'
WEBHOOK_URL = 'https://00103b68.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'state1',
        'state2',
        'play',
        'stay',
        'game',
        'sleep',
        'far',
        'near',
        'walk',
        'drive',
        'departmentstore',
        'park',
        'mountainclimbing',
        'Kaohsiung',
        'abroad',
        'aroundisland',
        'donothing'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state1',
            'conditions': 'is_going_to_state1'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'state2',
            'conditions': 'is_going_to_state2'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'play',
            'conditions': 'is_going_to_play'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'stay',
            'conditions': 'is_going_to_stay'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'donothing',
            'conditions': 'is_going_to_donothing'
        },
        {
            'trigger': 'advance',
            'source': 'play',
            'dest': 'far',
            'conditions': 'is_going_to_far'
        },
        {
            'trigger': 'advance',
            'source': 'play',
            'dest': 'near',
            'conditions': 'is_going_to_near'
        },
        {
            'trigger': 'advance',
            'source': 'far',
            'dest': 'abroad',
            'conditions': 'is_going_to_abroad'
        },
        {
            'trigger': 'advance',
            'source': 'far',
            'dest': 'aroundisland',
            'conditions': 'is_going_to_aroundisland'
        },
        {
            'trigger': 'advance',
            'source': 'near',
            'dest': 'walk',
            'conditions': 'is_going_to_walk'
        },
        {
            'trigger': 'advance',
            'source': 'walk',
            'dest': 'departmentstore',
            'conditions': 'is_going_to_departmentstore'
        },
        {
            'trigger': 'advance',
            'source': 'walk',
            'dest': 'park',
            'conditions': 'is_going_to_park'
        },
        {
            'trigger': 'advance',
            'source': 'near',
            'dest': 'drive',
            'conditions': 'is_going_to_drive'
        },
        {
            'trigger': 'advance',
            'source': 'drive',
            'dest': 'Kaohsiung',
            'conditions': 'is_going_to_Kaohsiung'
        },
        {
            'trigger': 'advance',
            'source': 'drive',
            'dest': 'mountainclimbing',
            'conditions': 'is_going_to_mountainclimbing'
        },
        {
            'trigger': 'advance',
            'source': 'stay',
            'dest': 'game',
            'conditions': 'is_going_to_game'
        },
        {
            'trigger': 'advance',
            'source': 'stay',
            'dest': 'sleep',
            'conditions': 'is_going_to_sleep'
        },
        {
            'trigger': 'go_back',
            'source': [
                'state1',
                'state2',
                'abroad',
                'aroundisland',
                'park',
                'mountainclimbing',
                'Kaohsiung',
                'sleep',
                'game',
                'departmentstore',
                'donothing'
            ],
            'dest': 'user'
        },

        ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
