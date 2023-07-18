from django_seed import Seed
from .models import *

def catblog_run():
    seeder = Seed.seeder()
    datas = [
        {
            'name' : 'Lifestyle'
        },
        {
            'name' : 'Design'
        }, 
        {
            'name' : 'Streetwear'
        }, 
        {
            'name' : 'Classics'
        },  
    ]
    for data in datas:
        seeder.add_entity(category_blog, 1, data)
    print(seeder.execute())


def blog_run():
    seeder = Seed.seeder()
    datas = [
        {
            'title' : 'behind the design', 
            'image' : 'https://static.nike.com/a/images/w_960,c_limit,f_auto/a5d3072e-5b8f-4ffd-8430-55d817e1b19f/behind-the-design-%E2%80%93-air-jordan%C2%A02-low-quai%C2%A054.png',
            'date' : '2023-07-10 11:51:37.576641',
            'job' : 'photographe',
            'name': 'jules',
            'description':'pLorem ipsum dolor sit amet consectetur adipisicing elit. Minima sunt modi atque aperiam saepe tempore? Culpa, eligendi odit? Praesentium accusamus, repellendus minus, aliquam dolores laboriosam, porro quos nobis harum quam aliquid. Voluptates, dolor molestias sapiente quidem cumque rerum recusandae numquam tempore explicabo vel est maxime, delectus perferendis quas cupiditate repellendus?',
            'catblog': category_blog.objects.get(id=1),
            
        },
        {
            'title' : 'on the ground', 
            'image' : 'https://static.nike.com/a/images/w_960,c_limit,f_auto/f334919d-524e-4186-b763-2ad32e4c8394/on-the-ground%C2%A0-cph-open%C2%A02023.jpg',
            'date' : '2023-08-10 10:51:37.476641',
            'job' : 'photographe',
            'name': 'marc',
            'description':'pLorem ipsum dolor sit amet consectetur adipisicing elit. Minima sunt modi atque aperiam saepe tempore? Culpa, eligendi odit? Praesentium accusamus, repellendus minus, aliquam dolores laboriosam, porro quos nobis harum quam aliquid. Voluptates, dolor molestias sapiente quidem cumque rerum recusandae numquam tempore explicabo vel est maxime, delectus perferendis quas cupiditate repellendus?',
            'catblog': category_blog.objects.get(id=2),
        },
        {
            'title' : "get 'em back in the game", 
            'image' : 'https://static.nike.com/a/images/w_960,c_limit,f_auto/9abbcf84-3c4e-45a3-9dce-b4b891224fe5/rafra%C3%AEchis-r%C3%A9invente-recycle-tes-affaires-avec-unknwn-projcts.jpg',
            'date' : '2023-02-10 11:51:37.576641',
            'job' : 'photographe',
            'name': 'julie',
            'description':'pLorem ipsum dolor sit amet consectetur adipisicing elit. Minima sunt modi atque aperiam saepe tempore? Culpa, eligendi odit? Praesentium accusamus, repellendus minus, aliquam dolores laboriosam, porro quos nobis harum quam aliquid. Voluptates, dolor molestias sapiente quidem cumque rerum recusandae numquam tempore explicabo vel est maxime, delectus perferendis quas cupiditate repellendus?',
            'catblog': category_blog.objects.get(id=3),
        },        
        {
            'title' : 'snkrs style', 
            'image' : 'https://static.nike.com/a/images/w_960,c_limit,f_auto/c98db9d2-d666-4981-b955-5143b6942149/snkrs-style%E2%80%8F%C2%A0-terminator-low-tola.jpg',
            'date' : '2023-03-08 11:51:37.576641',
            'job' : 'spencer',
            'name': 'jules',
            'description':'pLorem ipsum dolor sit amet consectetur adipisicing elit. Minima sunt modi atque aperiam saepe tempore? Culpa, eligendi odit? Praesentium accusamus, repellendus minus, aliquam dolores laboriosam, porro quos nobis harum quam aliquid. Voluptates, dolor molestias sapiente quidem cumque rerum recusandae numquam tempore explicabo vel est maxime, delectus perferendis quas cupiditate repellendus?',
            'catblog': category_blog.objects.get(id=4),
        },        
        {
            'title' : 'unmuted', 
            'image' : 'https://static.nike.com/a/images/w_960,c_limit,f_auto/357f2304-cd40-4ff4-a99c-916431e93996/cortez-unmuted-sound-system.jpg',
            'date' : '2023-04-06 11:51:37.576641',
            'job' : 'photographe',
            'name': 'lucas',
            'description':'pLorem ipsum dolor sit amet consectetur adipisicing elit. Minima sunt modi atque aperiam saepe tempore? Culpa, eligendi odit? Praesentium accusamus, repellendus minus, aliquam dolores laboriosam, porro quos nobis harum quam aliquid. Voluptates, dolor molestias sapiente quidem cumque rerum recusandae numquam tempore explicabo vel est maxime, delectus perferendis quas cupiditate repellendus?',
            'catblog': category_blog.objects.get(id=1),
        },
    ]
    for data in datas:
        seeder.add_entity(blog, 1, data)
    print(seeder.execute())