"""
URL configuration for projetfinal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from frontend.views import *
from products.views import *
from blog.views import *
from users.views import *
from backoffice.views import *
from contact.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('Products/', products, name='products'),
    path('Products/<int:product_id>/', add_to_cart, name='ajout-cart'),
    path('Products/destroy/<int:product_id>', remove_from_cart, name='destroy-cart'),
    path('Products/viewscart/', view_cart, name='cart-view'),
    path('Blog/', blog_page, name='blog'),
    path('details_blog/<int:id>', details_blog, name='details_blog'),
    path('Contact/', Contact_page, name='contact'),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'), 
    path('Products/<int:id>', show, name='details'),
    path('backoffice/', back_office, name='backoffice'),
    path('backoffice/back-products/', back_products, name='back-products'),
    path('backoffice/create-product/', productcreate, name='create-product'),
    path('backoffice/edit-product/<int:id>', editproduct, name='edit-product'),
    path('backoffice/back-products/destroy/<int:id>', productdestroy),
    path('backoffice/back-users/', back_users, name='back-users'),
    path('backoffice/edit-users/<int:id>', edituser, name='edit-user'),
    path('backoffice/back-users/destroy/<int:id>', Userdestroy),
    path('backoffice/back-blog/', back_blog, name='back-blog'),
    path('backoffice/create-blog/', blogcreate, name='create-blog'),
    path('backoffice/edit-blog/<int:id>', editblog, name='edit-blog'),
    path('backoffice/back-blog/destroy/<int:id>', blogdestroy),
    path('<path:invalid_path>', error_page, name='error_page'),
]