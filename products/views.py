from django.shortcuts import render, get_object_or_404, redirect
from .models import Products, Category , CartItem
from django.core.paginator import Paginator
from .models import CommentaryProduct
from .forms import CommentaryProductForm

def products(request):
    search = request.GET.get('search', '')
    sold = request.GET.get('sold')
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.total_price for item in cart_items)
    sneakers = Products.objects.filter(name__icontains=search)

    selected_category = request.GET.get('category')
    categorys = Category.objects.all()

    if selected_category:
        sneakers = sneakers.filter(category__name=selected_category)

    if sold == 'true':
        sneakers = sneakers.filter(discount__gt=0)

    # Calcul de la propriété discounted_price pour chaque produit
    for sneaker in sneakers:
        if sneaker.discount != 0:
            discount_amount = (sneaker.discount / 100) * sneaker.price
            sneaker.discounted_price = sneaker.price - discount_amount
        else:
            sneaker.discounted_price = sneaker.price

    paginator = Paginator(sneakers, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'projetfinal/products/products.html', {'sneakers': page_obj, 'categorys': categorys, 'selected_category': selected_category, "search": search, 'cart_items': cart_items, 'total_price': total_price})


def show(request, id):
    showsnkrs = Products.objects.get(id=id)
    # show = Product.objects.get(id=id)
    
    comments = CommentaryProduct.objects.filter(product=showsnkrs)
    if request.method == 'POST':
        form = CommentaryProductForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.product = showsnkrs
            new_comment.user = request.user
            new_comment.save()
        return redirect('details', id=show)
    else:
        form = CommentaryProduct()
        
    if request.user.is_authenticated:
        comment_form = CommentaryProductForm()
    else:
        comment_form = None

    
    return render(request, 'projetfinal/products/product-details.html', {"showsnkrs": showsnkrs, 'form': form, 'comment_form': comment_form, 'comments': comments})



def add_to_cart(request, product_id):
    product = get_object_or_404(Products, id=product_id)

    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))

        if product.stock >= quantity:
            # Vérifier si l'utilisateur est connecté, sinon rediriger vers la page de connexion
            if request.user.is_authenticated:
                cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
                cart_item.quantity += quantity
                cart_item.save()
            else:
                return redirect('login')  # Rediriger vers la vue de connexion si l'utilisateur n'est pas connecté

            # Enlevez la quantité du stock
            product.reduce_stock(quantity)

    return redirect('products')


def view_cart(request):
    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.total_price for item in cart_items)
    else:
        cart_items = []
        total_price = 0

    return render(request, 'projetfinal/cart/cart.html', {'cart_items': cart_items, 'total_price': total_price})

def remove_from_cart(request, product_id):
    cart_item = get_object_or_404(CartItem, id=product_id)

    # Vérifier que l'élément appartient à l'utilisateur connecté
    if request.user.is_authenticated and request.user == cart_item.user:
        cart_item.delete()

    return redirect('products')