import api
import os

def main():
    for a in range(1, 7):
        dev = '{}{}'.format("dev", a)
        root = api.path + '/%s/interviews/' % dev
        dirlist = [ item for item in os.listdir(root) if os.path.isfile(os.path.join(root, item)) ]
        for i in dirlist:
            if i.endswith('.mp3'):
                date = i[0:10].replace("_", "-")
                data_interview = {
                    "description": "Interview with {} on {}".format(dev,date),
                    "developer": api.get('developers', a),
                    "id": "",
                    "registred": date,
                    "tag": "Interview on " + date,
                    "author": "",
                    "license": ""
                }
                api.request("Interview", 'interviews', data_interview)

