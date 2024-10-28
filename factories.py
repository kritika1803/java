from faker import Faker
import random

fake = Faker()

def create_fake_product():
    return {
        "id": random.randint(1, 1000),
        "name": fake.word(),
        "category": fake.word(),
        "availability": random.choice([True, False]),
        "price": round(random.uniform(10, 100), 2)
    }
