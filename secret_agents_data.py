from faker import Faker
import random
from tabulate import tabulate

fake = Faker()

statuses = ('Active', 'Inactive', 'Retired', 'On Leave')
ranks = ('Agent', 'Senior Agent', 'Supervisor', 'Chief')

def generate_meeting_address():
    return f"{fake.street_address()}\n{fake.city()}, {fake.postcode()}"

agents_data = []

for i in range(101):
    agent = {
        'id': i,
        'alias': fake.user_name(),  
        'real_name': f"{fake.first_name()} {fake.last_name()}",  
        'rank': random.choice(ranks),  
        'status': random.choice(statuses),  
        'badge_number': fake.bothify(text='####-####'),  
        'meeting_location': generate_meeting_address(),  
        'contact_code': fake.numerify(text='#####')  
    }
    agents_data.append(agent)

table_data = []
for index, agent in enumerate(agents_data):
    if index <= 4 or index >= 96:
        row = [
            agent['id'],
            agent['alias'],
            agent['real_name'],
            agent['rank'],
            agent['status'],
            agent['badge_number'],
            agent['meeting_location'],
            agent['contact_code']
        ]
        table_data.append(row)
    elif index == 5:
        table_data.append(['...', '...', '...', '...', '...', '...', '...', '...'])

headers = [
    'ID',
    'Псевдоним',
    'Настоящее имя',
    'Звание',
    'Статус',
    'Номер значка',
    'Адрес явки',
    'Контактный код'
]

print(tabulate(table_data, headers, tablefmt="grid"))

import csv

keys = agents_data[0].keys()
with open('secret_service_agents.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(agents_data)
