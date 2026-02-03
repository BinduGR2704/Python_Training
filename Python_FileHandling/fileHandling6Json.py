import json

with open("sample.json", "r") as jsonFile:
    data = json.load(jsonFile)
    print(data)