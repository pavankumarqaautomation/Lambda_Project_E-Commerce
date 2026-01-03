import string
import random

def random_email():
    final=random.choices(string.ascii_letters,k=8)
    result="".join(final)+"@gmail.com"
    return result


def random_mobile_number():
    final=random.choices(string.digits,k=10)
    result="".join(final)
    return result


def random_password():
    strings=random.choices(string.ascii_letters,k=5)
    numbers=random.choices(string.digits,k=5)
    final=strings+numbers
    result="".join(final)
    return result

def random_first_name():
    final=random.choices(string.ascii_letters,k=5)
    result="".join(final)
    return result

def random_last_name():
    final=random.choices(string.ascii_letters,k=5)
    result="".join(final)
    return result

