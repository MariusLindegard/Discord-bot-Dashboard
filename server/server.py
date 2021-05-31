import json, codecs, time
from flask import Flask
app = Flask(__name__)

with codecs.open('bot_status.json','r', encoding='utf-8-sig') as File:
    config = json.load(File)


def update_config():
    with codecs.open('bot_status.json','r', encoding='utf-8-sig') as File:
        config = json.load(File)


def save_config():
    with codecs.open('bot_status.json', 'w', encoding='utf8') as File:
        json.dump(config, File, sort_keys=True, indent=4, ensure_ascii=False)


def shut_bot():
    if config["status"] == 'Shut down':
        statement = 'Bot has already been shut down'
    elif config["status"] == 'Running':
        statement = 'Shutting down bot'
        config["status"] = "Shut down"
        save_config()
    else:
        statement = 'Could not shut down bot'

    return statement

def starting_bot():
    if config["status"] == 'Shut down':
        statement = 'Bot is starting up'
        config["status"] = 'Start'
        save_config()
    else:
        statement = 'Could not start bot'

    return statement

@app.route('/shut')
def shutting_bot():
    update_config()
    return shut_bot()

@app.route('/start')
def start_bot():
    update_config()
    return starting_bot()

app.run(debug = True)