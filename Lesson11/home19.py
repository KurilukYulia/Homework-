import json
import csv
import random


def generate_number():
    return f"+380 {random.randint(1,100)} {random.randint(1,100)}-{random.randint(1,100)}-{random.randint(1,100)}"


with open('document_file.json') as json_file:
    input_data = json.load(json_file)


with open('new_document_file.csv', 'w', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)

    writer.writerow(['ID', 'Name', 'Age', 'Phone_number'])

    for id, info in input_data.items():
        phone_number = generate_number()
        writer.writerow([id, info[0], info[1], phone_number])
