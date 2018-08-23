import api

def main():
    data_design_pattern = {
        "id": "",
        "sourceCode": api.get('source-codes', 1),
        "status": "PRIVATE",
        "tag": "design pattern",
        "xmlDescriptor": "descriptor",
                    "author": "",
                    "license": ""
    }
    api.request("Design Pattern", 'design-patterns', data_design_pattern)