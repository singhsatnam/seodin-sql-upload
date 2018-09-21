import os
import api

def main():

    for a in range(1,7):
        dev = '{}{}'.format("dev", a)
        root = api.path + '/%s/interviews/' % dev
        root2 = api.path + '/%s/thinkalouds/' % dev
        dirlist1 = [item for item in os.listdir(root) if os.path.isfile(os.path.join(root, item))]
        dirlist2 = [item for item in os.listdir(root2) if os.path.isfile(os.path.join(root2, item))]
        for i in dirlist1:
            if i.endswith('.rtf'):
                data_note = {
                  "description": "Note from {} about System {}".format(dev, i[3]),
                  "id": "",
                  "interview": api.get('interviews', a),
                  "status": "PRIVATE",
                  "tag": i,
                  "thinkaloud": None,
                  "uri": "uri",
                  "author": "",
                  "license": ""
                }
                api.request("Note", 'notes', data_note)
        for i in dirlist2:
            if i.endswith('.doc' or '.xls'):
                data_note = {
                  "description": "Enter a description",
                  "id": "",
                  "interview": None,
                  "status": "PRIVATE",
                  "tag": i,
                  "thinkaloud": api.get('think-alouds', a),
                  "uri": "uri",
                  "author": "",
                  "license": ""
                }
                api.request("Note", 'notes', data_note)