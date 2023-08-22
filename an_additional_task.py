import random

def generate_email():
    login = 'vadim.kotyukov.12'
    numbers = str(random.randint(100, 999))
    domen = '@ya.ru'
    email = login + numbers + domen
    return email




def generate_password():
    password = str(random.randint(100000, 999999))
    return password
