import api

def main():
    data_software_system = {
        "id": "",
        "study": api.get('studies', 1),
        "tag": "System A"
    }
    api.request("Sofware System", 'software-systems', data_software_system)

    data_software_system = {
        "id": "",
        "study": api.get('studies', 1),
        "tag": "System B",
        "author": "",
        "license": ""
    }
    api.request("Sofware System", 'software-systems', data_software_system)

    data_software_system = {
        "id": "",
        "study": api.get('studies', 1),
        "tag": "System C",
        "author": "",
        "license": ""
    }
    api.request("Sofware System", 'software-systems', data_software_system)

    data_software_system = {
        "id": "",
        "study": api.get('studies', 1),
        "tag": "System D",
        "author": "",
        "license": ""
    }
    api.request("Sofware System", 'software-systems', data_software_system)
