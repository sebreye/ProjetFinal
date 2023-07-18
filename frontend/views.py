from django.shortcuts import render
from .models import background_index, background2
from products.models import Products
from blog.models import blog
from django.db.models import Count
# Create your views here.
def home(request): 
    snkrs = Products.objects.all().order_by('-id')[:6]
    backgrounds = background_index.objects.all()
    backsmid = background2.objects.all()
    recentposts = blog.objects.all().order_by('-date')[:3]
    products = Products.objects.annotate(comment_count=Count('commentaryproduct'))
    products = products.order_by('-comment_count')
    return render(request, 'projetfinal/frontend/home.html', {'backgrounds': backgrounds, 'backsmid': backsmid, 'snkrs': snkrs, 'recentposts': recentposts, 'products': products})
def error_page(request, invalid_path):
    return render(request, 'projetfinal/frontend/error-404.html', {'invalid_path': invalid_path})