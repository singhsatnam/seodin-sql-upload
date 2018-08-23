import api

def main():
    data_task = {
        "id": "",
        "study": api.get('studies', 1),
        "tag": "Maintenance adaptative platform adjustment 1",
        "author": "",
        "license": ""

    }
    api.request("Task", 'tasks', data_task)

    data_task = {
        "id": "",
        "study": api.get('studies', 1),
        "tag": "Maintenance adaptative platform adjustment 2",
        "author": "",
        "license": ""
    }
    api.request("Task", 'tasks', data_task)

    data_task = {
        "id": "",
        "study": api.get('studies', 1),
        "tag": "Maintenance perfective",
        "author": "",
        "license": ""
    }
    api.request("Task", 'tasks', data_task)