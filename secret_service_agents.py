from faker import Faker
import random
from faker.providers import DynamicProvider
from tabulate import tabulate

# Инициализация Faker
fake = Faker()

# Создаем динамический провайдер для статусов агентов
statuses_provider = DynamicProvider(
    provider_name="agent_statuses",
    elements=["Active", "Inactive", "Retired", "On Leave"]
)
fake.add_provider(statuses_provider)

# Создаем динамический провайдер для званий
ranks_provider = DynamicProvider(
    provider_name="agent_ranks",
    elements=["Agent", "Senior Agent", "Supervisor", "Chief"]
)
fake.add_provider(ranks_provider)

# Генерация случайных данных
cardinality = 101  # Количество записей

# Исправленная генерация ID удостоверений
badge_numbers = [f"{random.randint(1000, 9999)}-{random.randint(1000, 9999)}" for _ in range(cardinality)]

# Генерация данных
agents_data = [
    {
        'id': i,
        'alias': fake.user_name(),
        'real_name': f"{fake.first_name()} {fake.last_name()}",
        'rank': fake.agent_ranks(),
        'status': fake.agent_statuses(),
        'badge_number': badge_numbers[i],
        'meeting_location': fake.address(),
        'contact_code': fake.numerify('#####')
    }
    for i in range(cardinality)
]

# Формируем данные для таблицы
table_data = [
    [
        entry['id'],
        entry['alias'],
        entry['real_name'],
        entry['rank'],
        entry['status'],
        entry['badge_number'],
        entry['meeting_location'],
        entry['contact_code']
    ]
    for entry in agents_data
]

# Добавляем нумерацию
numbered_data = [i+1] + row for i, row in enumerate(table_data)

# Заголовки таблицы
headers = ['№', 'ID', 'Псевдоним', 'Настоящее имя', 'Звание', 'Статус', 'Номер значка', 'Адрес явки', 'Код контакта']

# Выводим таблицу
print(tabulate(numbered_data[:5], headers, tablefmt="grid"))
print("\n...\n")
print(tabulate(numbered_data[96:], headers, tablefmt="grid"))

# Сохраняем в CSV
import csv

keys = agents_data[0].keys()
with open('secret_service_agents.csv', 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    writer.writeheader()
    writer.writerows(agents_data)
