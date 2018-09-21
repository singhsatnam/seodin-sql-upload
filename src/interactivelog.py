import os
import csv
import api

def main():
    devs = api.getAll('developers')
    for a in range(1,7):
        dev = '{}{}'.format("dev", a)
        root = api.path + '/%s/logs/1-original/' % dev
        dirlist = [item for item in os.listdir(root) if os.path.isfile(os.path.join(root, item))]
        for i in dirlist:
            date = i[0:10].replace("_", "-")
            with open(root + i, "rU") as f:
                reader = csv.reader(f, delimiter = "\t")
                data = list(reader)
                y = 0
                while y < len(data):

                    #First exception : comma at end of cell
                    if str(data[y]).endswith(",']"):
                        _list = (str(data[y]).replace(",']","']")).split(",")
                    else:
                        _list = str(data[y]).split(",")

                    #Second exception : other commas in cell
                    if len(_list) > 6:
                        _list[4] = _list[4][:-1]
                        for x in range(5, len(_list)-1):
                            if _list[x].startswith(" '"):
                                cropped_list = " " + _list[x][2:]
                            else:
                                cropped_list = "," + _list[x][1:]
                            _list[4] = _list[4] + cropped_list
                        _list[5] = _list[-1]

                    data_interactive_log = {
                        "delta": _list[5][8:][:-3],
                        "developer": devs[a-1],
                        "id": "",
                        "kind": _list[2][7:].upper(),
                        "origin": _list[4][9:],
                        "registred": date,
                        "sourceHandle": _list[3][15:],
                        "status": "PRIVATE",
                        "author": "",
                        "license": ""
                    }
                    api.request("Interactive Log", 'interactive-logs', data_interactive_log)
                    y = y + 1