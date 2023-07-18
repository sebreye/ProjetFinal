from django_seed import Seed
from .models import *
from django.contrib.auth.hashers import make_password

def user_run():
    seeder = Seed.seeder()

    users = [
        {'username': 'member', 'email': 'member@member.com', 'password': make_password('1234'), 'role': 'Membre'},
        {'username': 'admin', 'email': 'admin@admin.com', 'password': make_password('1234'), 'role': 'Admin'},
        {'username': 'web', 'email': 'web@web.com', 'password': make_password('1234'), 'role': 'Webmaster'},
        {'username': 'stock', 'email': 'stock@stock.com', 'password': make_password('1234'), 'role': 'Stocker'},
    ]

    for item in users:
        seeder.add_entity(Users, 1, item)

    print(seeder.execute())