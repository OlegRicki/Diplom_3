import faker

fake = faker.Faker()


def generate_user_name() -> str:
    return fake.user_name()

