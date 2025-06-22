from faker import Faker
import random

fake = Faker()

statuses = ['Active', 'Inactive', 'Retired', 'On Leave']

ranks = ['Agent', 'Senior Agent', 'Supervisor', 'Chief']

def generate_meeting_address():
    return f"{fake.street_address()}\n{fake.city()}, {fake.postcode()}"

agents_data = []

for i in range(100):
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

for agent in agents_data[:10]:
    print(f"ID: {agent['id']}")
    print(f"Псевдоним: {agent['alias']}")
    print(f"Настоящее имя: {agent['real_name']}")
    print(f"Звание: {agent['rank']}")
    print(f"Статус: {agent['status']}")
    print(f"Номер значка: {agent['badge_number']}")
    print(f"Адрес явки: {agent['meeting_location']}")
    print(f"Контактный код: {agent['contact_code']}")
    print("-" * 40)

import csv

keys = agents_data[0].keys()
with open('secret_service_agents.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(agents_data)
