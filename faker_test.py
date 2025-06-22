from faker import Faker

fake = Faker()

def generate_basic_data():
    return {
        'name': fake.name(),
        'address': fake.address(),
        'email': fake.email(),
        'phone_number': fake.phone_number(),
        'text': fake.text()
    }

if __name__ == "__main__":
    print("Генерация базовых данных:")
    print(generate_basic_data())

def generate_localized_data():
    fake_it = Faker('it_IT')
    print("Итальянская локализация:")
    print(fake_it.name())
    
    fake_multi = Faker(['it_IT', 'en_US', 'ja_JP'])
    print("\nМногоязычная локализация:")
    for _ in range(3):
        print(fake_multi.name())

generate_localized_data()

from faker.providers import internet

fake.add_provider(internet)

def generate_internet_data():
    return {
        'ipv4': fake.ipv4_private(),
        'domain_name': fake.domain_name(),
        'url': fake.url()
    }

print("\nГенерация интернет-данных:")
print(generate_internet_data())

def generate_unique_data():
    unique_names = [fake.unique.name() for _ in range(5)]
    print("\nУникальные имена:")
    print(unique_names)

generate_unique_data()

def generate_reproducible_data():
    Faker.seed(4321)
    print("\nВоспроизводимые данные:")
    print(fake.name())
    print(fake.address())

generate_reproducible_data()
