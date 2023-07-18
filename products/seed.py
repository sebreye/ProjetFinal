from django_seed import Seed
from .models import Products, Category

def category_run():
    seeder = Seed.seeder()
    datas = [
        {
            'name': 'summer'
        },
        {
            "name": 'winter'
        }, 
        {
            'name': 'springs'
        }, 
        {
            'name': 'autumn'
        }

    ]
    for data in datas:
        seeder.add_entity(Category, 1, data)
    
    print(seeder.execute())
def products_run():
    seeder = Seed.seeder()
    datas = [
        {
            'name': 'Air Jordan 2 Retro Low quai 54',
            'price': 110,
            'image1': 'https://secure-images.nike.com/is/image/DotCom/FN7686_100_A_PREM?$SNKRS_COVER_WD$&align=0,1',
            'image2': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/f3ec7613-701c-4db6-97f0-34fa2c796a74/air-jordan%C2%A02-retro-low-«%C2%A0quai%C2%A054%C2%A0»-fn7686-100.jpg',
            'image3': 'https://static.nike.com/a/images/t_prod_sc/w_640,c_limit,f_auto/1e987102-a0c0-4785-918c-786ff692fe99/air-jordan%C2%A02-retro-low-«%C2%A0quai%C2%A054%C2%A0»-fn7686-100.jpg',
            'category': Category.objects.get(id=2),
            'gender': 'M',
            'description': 'Description 1',
            'discount': 40,
            'stock38': 5,
            'stock39': 10,
            'stock40': 8,
            'stock41': 3,
            'stock42': 15,
            'stock43': 20,
            'stock44': 12,
            'stock45': 6,
        },
        {
            'name': 'Nike Terminator Low phantom',
            'price': 120,
            'image1': 'https://secure-images.nike.com/is/image/DotCom/FJ4207_001_A_PREM?$SNKRS_COVER_WD$&align=0,1',
            'image2': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/b437b12f-15c3-4f47-b36c-008712119daa/nike-terminator-low-«%C2%A0phantom%C2%A0»-fj4207-001.jpg',
            'image3': 'https://static.nike.com/a/images/t_prod_sc/w_640,c_limit,f_auto/64ff14f8-0e46-4305-ba68-ad2d4e38ad90/nike-terminator-low-«%C2%A0phantom%C2%A0»-fj4207-001.jpg',
            'category': Category.objects.get(id=3),
            'gender': 'F',
            'description': 'Description 2',
            'discount': 25,
            'stock38': 10,
            'stock39': 5,
            'stock40': 20,
            'stock41': 15,
            'stock42': 10,
            'stock43': 8,
            'stock44': 3,
            'stock45': 18,
        },
        {
            'name': 'Air Jordan 1 Black and Smoke Grey',
            'price': 150,
            'image1': 'https://secure-images.nike.com/is/image/DotCom/DZ5485_051_A_PREM?$SNKRS_COVER_WD$&align=0,1',
            'image2': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/80c358e0-91e1-4197-8126-0e06d87ab850/date-de-sortie-de-la-air-jordan%C2%A01-«%C2%A0black-and-smoke-grey%C2%A0»-dz5485-051.jpg',
            'image3': 'https://static.nike.com/a/images/t_prod_sc/w_640,c_limit,f_auto/6dd77102-ae31-4c38-a339-f70378d6268e/date-de-sortie-de-la-air-jordan%C2%A01-«%C2%A0black-and-smoke-grey%C2%A0»-dz5485-051.jpgx   ',
            'category': Category.objects.get(id=3),
            'gender': 'M',
            'description': 'Description 1',
            'discount': 50,
            'stock38': 5,
            'stock39': 10,
            'stock40': 8,
            'stock41': 3,
            'stock42': 15,
            'stock43': 20,
            'stock44': 12,
            'stock45': 6,
        },  
        {
            'name': 'Air Jordan 1 Low Black Cement',
            'price': 125,
            'image1': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/c5aa0e2f-2b31-44d3-b1ec-bb3a04637e4c/date-de-sortie-de-la-air-humara-«%C2%A0black-and-metallic-silver%C2%A0»-fj7098-002.jpg',
            'image2': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/5d397d37-71e1-45bf-815e-f55986f961dc/date-de-sortie-de-la-air-humara-«%C2%A0black-and-metallic-silver%C2%A0»-fj7098-002.jpg',
            'image3': 'https://static.nike.com/a/images/t_prod_sc/w_640,c_limit,f_auto/60f7860e-64ef-4445-9352-0ee97a0e9ba4/date-de-sortie-de-la-air-humara-«%C2%A0black-and-metallic-silver%C2%A0»-fj7098-002.jpgx@',
            'category': Category.objects.get(id=1),
            'gender': 'M',
            'description': 'Description 1',
            'discount': 0,
            'stock38': 5,
            'stock39': 10,
            'stock40': 8,
            'stock41': 3,
            'stock42': 15,
            'stock43': 20,
            'stock44': 12,
            'stock45': 6,
        },
        {
            'name': 'Air Humara Black and Metallic Silver',
            'price': 140,
            'image1': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/214d7d9f-7fd5-4864-a884-9af6ad9cd221/date-de-sortie-de-la-air-jordan%C2%A01-low-«%C2%A0black-cement%C2%A0»-cz0790-001.jpg',
            'image2': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/cc3fd81c-3886-499b-bc71-824b828c275d/date-de-sortie-de-la-air-jordan%C2%A01-low-«%C2%A0black-cement%C2%A0»-cz0790-001.jpg',
            'image3': 'https://static.nike.com/a/images/t_prod_sc/w_640,c_limit,f_auto/0838ac6f-56ab-4026-936b-43d81f21d74d/date-de-sortie-de-la-air-jordan%C2%A01-low-«%C2%A0black-cement%C2%A0»-cz0790-001.jpg',
            'category': Category.objects.get(id=2),
            'gender': 'M',
            'description': 'Description 1',
            'discount': 0,
            'stock38': 5,
            'stock39': 10,
            'stock40': 8,
            'stock41': 3,
            'stock42': 15,
            'stock43': 20,
            'stock44': 12,
            'stock45': 6,
        },
        {
            'name': 'Air Humara Black and Metallic Silver',
            'price': 130,
            'image1': 'https://secure-images.nike.com/is/image/DotCom/DV7525_001_A_PREM?$SNKRS_COVER_WD$&align=0,1',
            'image2': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/8757ffee-38ac-42b8-acd7-a2d60e17af0d/date-de-sortie-de-la-air-max%C2%A01%C2%A0-86-«%C2%A0lost-sketch%C2%A0»-dv7525-001.jpg',
            'image3': 'https://static.nike.com/a/images/t_prod_sc/w_640,c_limit,f_auto/9e69dda5-4cfd-48c1-a134-49ba3af1d835/date-de-sortie-de-la-air-max%C2%A01%C2%A0-86-«%C2%A0lost-sketch%C2%A0»-dv7525-001.jpg',
            'category': Category.objects.get(id=1),
            'gender': 'M',
            'description': 'Description 1',
            'discount': 0,
            'stock38': 5,
            'stock39': 10,
            'stock40': 8,
            'stock41': 3,
            'stock42': 15,
            'stock43': 20,
            'stock44': 12,
            'stock45': 6,
        },
        {
            'name': 'Air Jordan 2 Retro Low quai 54',
            'price': 122,
            'image1': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/31067687-75d2-405a-aa09-19f6562335fb/date-de-sortie-de-la-air-jordan%C2%A04-«%C2%A0canyon-purple%C2%A0»-pour-femme-aq9129-500.jpg',
            'image2': 'https://static.nike.com/a/images/t_prod_ss/w_640,c_limit,f_auto/177788b7-a76d-45bc-b57b-89c4efb3b8a3/date-de-sortie-de-la-air-jordan%C2%A04-«%C2%A0canyon-purple%C2%A0»-pour-femme-aq9129-500.jpg',
            'image3': 'https://static.nike.com/a/images/t_prod_sc/w_640,c_limit,f_auto/b53fa318-405a-40b9-8679-cfe1253fd368/date-de-sortie-de-la-air-jordan%C2%A04-«%C2%A0canyon-purple%C2%A0»-pour-femme-aq9129-500.jpg',
            'category': Category.objects.get(id=4),
            'gender': 'F',
            'description': 'Description 1',
            'discount': 25,
            'stock38': 5,
            'stock39': 10,
            'stock40': 8,
            'stock41': 3,
            'stock42': 15,
            'stock43': 20,
            'stock44': 12,
            'stock45': 6,
        },
]
    for data in datas:
        seeder.add_entity(Products, 1, data)
    
    print(seeder.execute())