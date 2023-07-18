from django.shortcuts import render
from .models import blog, category_blog
from django.core.paginator import Paginator
# Create your views here.
def blog_page(request):
    selected_category = request.GET.get('category')
    categories = category_blog.objects.all()
    articles = blog.objects.all()
    popularposts = blog.objects.all().order_by('date')[:3]
    
    if selected_category:
        articles = articles.filter(catblog__name=selected_category)
    
    paginator = Paginator(articles, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'projetfinal/blog/blog.html', {'articles': page_obj, 'categories': categories, 'popularposts': popularposts, 'selected_category': selected_category})


def details_blog(request, id):
    showposts = blog.objects.get(id=id)
    return render(request, 'projetfinal/blog/details-blog.html', {'showposts':showposts})

