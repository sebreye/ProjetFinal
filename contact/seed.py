from django_seed import Seed
from .models import *

def AboutUs_run():
    seeder = Seed.seeder()
    datas = [
        {
            "location": "Sample Location 1",
            "phone": "+1234567890",
            "email": "sample1@example.com",
            "fax": "+0987654321",
        },
    ]
    for data in datas:
        seeder.add_entity(AboutUs, 1, data)
    print(seeder.execute())
