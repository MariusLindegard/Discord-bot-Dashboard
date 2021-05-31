import json, codecs, time, os
from bot import main

os.system('start_server.sh')

def save_config():
    with codecs.open('bot_status.json', 'w', encoding='utf8') as File:
        json.dump(config, File, sort_keys=True, indent=4, ensure_ascii=False)

while True:
    time.sleep(0.5)
    with codecs.open('bot_status.json','r', encoding='utf-8-sig') as File:
        config = json.load(File)
    if config["status"] == 'Start':
        config["status"] = 'Running'
        save_config()
        main.run()