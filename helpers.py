import datetime
import random
import uuid

from faker import Faker

fake = Faker("ru_RU")


def generate_first_name():
    return fake.first_name()


def generate_password():
    return f"Pwd_{uuid.uuid4().hex[:10]}!"


def generate_login():
    return f"courier_{uuid.uuid4().hex[:12]}"


def generate_last_name():
    return fake.last_name()


def generate_address():
    return fake.street_address()


def generate_metro_station():
    return random.randint(1, 5)


def generate_phone():
    return "+79" + "".join(str(random.randint(0, 9)) for _ in range(9))


def generate_rent_time():
    return random.randint(1, 5)


def generate_delivery_date():
    return str(datetime.date.today())


def generate_comment():
    return fake.text(max_nb_chars=100)


def generate_color():
    return [random.choice(["BLACK", "GREY"])]


def generate_limit_orders():
    return random.randint(2, 11)


def generate_courier_id():
    return random.randint(99999, 999999)