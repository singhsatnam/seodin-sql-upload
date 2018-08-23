import os
import api

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
        root = api.path + '%s/testing' % dev
        dirlist = [ item for item in os.listdir(root) if os.path.isfile(os.path.join(root, item)) ]
        for i in dirlist:
            index = checkSystem(i)
            data_test_case = {
                "developer": api.get('developers', a),
                "id": "",
                "softwareSystem": api.get('software-systems', index),
                "status": "PRIVATE",
                "tag": i,
                "uri": "http://opendata.soccerlab.polymtl.ca/test-cases/" + i,
                "author": "",
                "license": ""
            }
            api.request("Test case", 'test-cases', data_test_case)