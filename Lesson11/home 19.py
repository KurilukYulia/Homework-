import json


with open('document_file.json')as file:
    input_data = json.load(file)

keys = ["ID", "name", "age", "number"]
data_rows = []
for item in input_data:
    data = []
    for key in keys:
        data.append(data.get(key))
    data_rows.append(data)

print(data_rows)

