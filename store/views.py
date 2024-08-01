from django.shortcuts import render
from django.shortcuts import render , get_object_or_404
from .models import Product
from cart.models import CartItem
from categories.models import Categories

# Create your views here.
def store(request, category_slug=None,cart_cost=0,cart_items=0):
    category = None
    products = None
    cart_cost = 2000
    cart_items = 5

    if category_slug != None:
        category = get_object_or_404(Categories, slug=category_slug )
        products = Product.objects.filter(category=category , is_available= True) 
        product_count = products.count()
    else:
        products = Product.objects.all().filter(is_available= True)
        product_count = products.count()

    context = {
        'products' : products,
        'product_count' : product_count,
        'category' : category,
        'selcted_slug' : category_slug,
        'cart_cost': cart_cost,
        'cart_items': cart_items,
        'total_items': len(CartItem.objects.all()),
    }

    return render(request, "store/store.html", context)
