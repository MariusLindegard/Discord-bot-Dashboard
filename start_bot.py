import json, codecs, time, os, datetime
from bot import main
from termcolor import colored

with codecs.open('bot_status.json','r', encoding='utf-8-sig') as File:
    config = json.load(File)


def start_bot():
    main.run()

def save_config():
    with codecs.open('bot_status.json', 'w', encoding='utf8') as File:
        json.dump(config, File, sort_keys=True, indent=4, ensure_ascii=False)

if config["flask"] == 'Not running':
    os.system('start cmd /c python server/server.py')
    config["flask"] = 'Running'
    save_config()

while True:
    with codecs.open('bot_status.json','r', encoding='utf-8-sig') as File:
        config = json.load(File)
    time.sleep(3)

    if config["status"] == 'Start':
        config["status"] = 'Running'
        save_config()
        print(colored('----STARTING DISCORD BOT----', 'green'))
        startup_time = datetime.datetime.now()
        print(startup_time.strftime("Time: %H:%M:%S"))
        print()

        start_bot()
    elif config["status"] == 'Restart Server' or config["status"] == "Clean start":
        config["status"] = 'Start'
        save_config()
        os.system('python restart_server.py')
        exit()

    elif config["status"] == 'Shut down main':
        config["status"] = 'Start'
        save_config()
        exit()
        
    print('Loop running')