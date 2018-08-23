import api

def main():
    data_source_code = {
        "id": "",
        "softwareSystem": api.get('software-systems', 1),
        "status": "PRIVATE",
        "tag": "Source code",
        "uri": "uri",
        "author": "",
        "license": ""
    }
    api.request("Source Code", 'source-codes', data_source_code)