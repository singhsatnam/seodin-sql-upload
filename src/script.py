import api

def main():
    data_script = {
      "description": "Enter a description",
      "id": "",
      "sourceCode": "Code",
      "status": "PRIVATE",
      "tag": "string",
      "author": "",
      "license": ""
    }
    api.request("Script", 'scripts', data_script)