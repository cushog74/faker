from faker import Faker
import random
from tabulate import tabulate

# Инициализация Faker
fake = Faker()

# Определяем возможные статусы и ранги
statuses = ('Active', 'Inactive', 'Retired', 'On Leave')
ranks = ('Agent', 'Senior Agent', 'Supervisor', 'Chief')

# Функция для генерации адреса явки
def generate_meeting_address():
    return f"{fake.street_address()}\n{fake.city()}, {fake.postcode()}"

# Создаем список для хранения данных
agents_data = []

# Генерируем 101 запись
for i in range(101):
    agent = {
        'id': i,
        'alias': fake.user_name(),  # Псевдоним агента
        'real_name': f"{fake.first_name()} {fake.last_name()}",  # Настоящее имя
        'rank': random.choice(ranks),  # Звание
        'status': random.choice(statuses),  # Статус
        'badge_number': fake.bothify(text='####-####'),  # Номер значка
        'meeting_location': generate_meeting_address(),  # Адрес явки
        'contact_code': fake.numerify(text='#####')  # Контактный код
    }
    agents_data.append(agent)

# Формируем данные для таблицы
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
        # Добавляем строку с многоточием
        table_data.append(['...', '...', '...', '...', '...', '...', '...', '...'])

# Заголовки таблицы
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

# Выводим таблицу в формате grid
print(tabulate(table_data, headers, tablefmt="grid"))

# Сохраняем в CSV файл
import csv

keys = agents_data[0].keys()
with open('secret_service_agents.csv', 'w', newline='', encoding='utf-8') as output_file:
    dict_writer = csv.DictWriter(output_file, fieldnames=keys)
    dict_writer.writeheader()
    dict_writer.writerows(agents_data)
