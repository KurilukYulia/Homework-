import json

document = { 123456: ("Ania", 23), 789564: ("Bob", 18), 234780: ("Mia", 17), 785612: ("Ken", 28),987634: ("Inna", 45),567341: ("Karl", 34)}

with open('document_file.json', 'w') as file:
    json.dump(document, file)
