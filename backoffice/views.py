from django.shortcuts import render, redirect
from users.models import Users
from users.forms import InscriptionForm
from products.models import Products, Category
from products.forms import ProductForm
from blog.models import blog
from .forms import blogForm
# Create your views here.
def back_office(request):
    return render(request, 'projetfinal/backend/backoffice.html')




def back_products(request):
    categories = Category.objects.all()
    allproducts = Products.objects.all()
    return render(request, 'projetfinal/backend/back-products/back-products.html', {'allproducts': allproducts, 'categories': categories})
def editproduct(request, id):
    edit = Products.objects.get(id=id)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = ProductForm(instance=edit)
    return render(request, 'projetfinal/backend/back-products/edit-products.html', {'form': form})
def productcreate(request):
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = ProductForm()
    return render(request, 'projetfinal/backend/back-products/create-products.html', {'form': form})
def productdestroy(request, id):
    destroy = Products(id)
    destroy.delete()
    return redirect('backoffice')





def back_users(request):
    allmembers = Users.objects.all()
    return render(request, 'projetfinal/backend/back-users/back-users.html', {'allmembers': allmembers})
def edituser(request, id):
    edit = Users.objects.get(id=id)
    if request.method == 'POST':
        form = InscriptionForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = InscriptionForm(instance=edit)
    return render(request, 'projetfinal/backend/back-users/edit-users.html', {'form': form})
def Userdestroy(request, id):
    destroy = Users(id)
    destroy.delete()
    return redirect('backoffice')



    
def back_blog(request):
    allblogs = blog.objects.all()
    return render(request, 'projetfinal/backend/back-blog/back-blog.html', {'allblogs': allblogs})
def editblog(request, id):
    edit = blog.objects.get(id=id)
    if request.method == 'POST':
        form = blogForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = blogForm(instance=edit)
    return render(request, 'projetfinal/backend/back-blog/edit-blog.html', {'form': form})
def blogcreate(request):
    if request.method == 'POST':
        form = blogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('backoffice')
    else:
        form = blogForm()
    return render(request, 'projetfinal/backend/back-blog/create-blog.html', {'form': form})
def blogdestroy(request, id):
    destroy = blog(id)
    destroy.delete()
    return redirect('backoffice')