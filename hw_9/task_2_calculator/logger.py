import json
from datetime import datetime

def logging(text):
    file = open('log.json', 'a', encoding='utf-8')
    time = str(datetime.now())
    new = {'time': time, 'result': text}
    json.dump(new, file, indent=1)
    file.close()

# logging('4+2')