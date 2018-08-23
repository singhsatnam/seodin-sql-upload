import api
import os

def checkSystem(i):
    if i[3] == 'A':
        return 1
    elif i[3] == 'B':
        return 2
    elif i[3] == 'C':
        return 3
    elif i[3] == 'D':
        return 4

def main():
    for a in range(1,7):
        dev = '{}{}'.format("dev", a)
        root = api.path + '%s/thinkalouds/' % dev
        dirlist = [item for item in os.listdir(root) if os.path.isfile(os.path.join(root, item))]
        for i in dirlist:
            if i.endswith('.avi'):
                index = checkSystem(i)
                date = i[16:26].replace("_", "-")
                data_think_aloud = {
                    "description": "Think-aloud from {} on {}".format(dev, date),
                    "developer": api.get('developers', a),
                    "id": "",
                    "registred": date,
                    "softwareSystem": api.get('software-systems', index),
                    "tag": "Think aloud on " + date,
                    "author": "",
                    "license": ""
                }
                api.request("Think Aloud", 'think-alouds', data_think_aloud)