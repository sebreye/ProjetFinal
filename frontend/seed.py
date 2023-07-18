from django_seed import Seed
from .models import background_index, background2
def background_run():
    seeder = Seed.seeder()
    datas = [
        {
            'backimage' : 'https://media.gq-magazine.co.uk/photos/5fc8a778ea31983340383042/16:9/w_2560%2Cc_limit/03112020_Drake_02.jpg'
        },
        {
            'backimage' : 'https://mir-s3-cdn-cf.behance.net/project_modules/1400/c20f0e63226021.61cb9889bc541.png'
        }, 
        {
            'backimage' : 'https://cdn.shopify.com/s/files/1/0270/5326/0848/files/Image_5_copy_1e89c4e1-00f3-4c8d-8fb5-c16106582ade_1024x1024.jpg?v=1674052340'
        }, 
    ]
    for data in datas:
        seeder.add_entity(background_index, 1, data)
    print(seeder.execute())

def background2_run():
    seeder = Seed.seeder()
    datas = [
        {
            'background' : 'https://w0.peakpx.com/wallpaper/939/841/HD-wallpaper-nike-water.jpg'
        },
    ]
    for data in datas:
        seeder.add_entity(background2, 1, data)
    print(seeder.execute())