import os
import api
import datetime
date = (datetime.datetime.now()).strftime("%Y-%m-%d")

def main():
    total = 0

    #LINK WITH TASK

    for a in range(1,7):
        dev = '{}{}'.format("dev", a)
        root = api.path + '%s/diaries' % dev
        dirlist = [ item for item in os.listdir(root) if os.path.isfile(os.path.join(root, item)) ]
        for i in dirlist:
            data_diary = {
                "developer": api.get('developers', a),
                "id": "",
                "registred": date,
                "softwareSystem": api.get('software-systems', 1),
                "status": "PRIVATE",
                "task": None, #???
                "uri": "uri",
                "author": "",
                "license": ""
            }
            api.request("Diary", 'diaries', data_diary)
            total = total + 1
