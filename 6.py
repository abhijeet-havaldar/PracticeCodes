import json

data = {'a': 1, 'b': 2}
with open('data.json', 'w') as file:
    json.dump(data, file)
with open('data.json', 'r') as file:
    print(json.load(file).get('b',0))