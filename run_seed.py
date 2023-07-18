import django
django.setup()

from products.seed import *
from blog.seed import *
from frontend.seed import *
from users.seed import *
from contact.seed import *
if __name__ == '__main__':
    # category_run()
    # products_run()
    # catblog_run()
    # tagblog_run()
    # blog_run()
    # background_run()
    # background2_run()
    # user_run()
    AboutUs_run()
