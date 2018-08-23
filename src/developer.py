import os
import api

def main():
    root = api.path
    dirlist = [ item for item in os.listdir(root) if os.path.isdir(os.path.join(root, item)) ]
    for i in dirlist:
        data_developer = {
            "id": "",
            "name": i,
            "study": api.get('studies', 1),
            "license": ""
        }
        api.request(i, 'developers', data_developer)