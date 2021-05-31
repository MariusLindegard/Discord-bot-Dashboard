import json, codecs
from flask import Flask, request, render_template
#from flask import request
app = Flask(
    __name__,
    template_folder='style',
    static_folder='static'
    )


def update_config():
    with codecs.open('bot_status.json','r', encoding='utf-8-sig') as File:
        config = json.load(File)
    return config


def save_config(config):
    with codecs.open('bot_status.json', 'w', encoding='utf8') as File:
        json.dump(config, File, sort_keys=True, indent=4, ensure_ascii=False)

def shutdown_server(config):
    config["flask"] = 'Not running'
    config["status"] = 'Shut down main'
    save_config()
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

def shut_bot(config):
    if config["status"] == 'Shut down':
        statement = 'Bot has already been shut down'
    elif config["status"] == 'Running':
        statement = 'Shutting down bot'
        config["status"] = "Shut down"
        save_config(config)
    else:
        statement = 'Could not shut down bot'

    return statement

def restart_bot(config):
    if config["status"] == 'Running':
        statement = 'Restarting bot'
        config["status"] = 'Restart'
        save_config(config)
    else:
        statement = 'Could not restart'
    
    return statement

def starting_bot(config):
    if config["status"] == 'Stopped':
        statement = 'Bot is starting up'
        config["status"] = 'Clean start'
        save_config(config)
    else:
        statement = 'Could not start bot'

    return statement

@app.route('/restart')
def restart():
    return restart_bot(update_config())

@app.route('/shut')
def shutting_bot():
    return shut_bot(update_config())

@app.route('/start')
def start_bot():
    return starting_bot(update_config())

@app.route('/shutdown')
def stop_server():
    shutdown_server(update_config())
    return 'Server shutting down...'

@app.route('/')
@app.route('/home')
def home_page():
    return render_template("index.html", title="Colosseum RP Discord bot dashboard", username="MelonKami")

if __name__ == "__main__":
    app.run(debug = True)