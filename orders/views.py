from django.shortcuts import redirect, render, get_object_or_404
from products.models import Product
from django.contrib import messages
from .models import Order, OrderItem
from .cart import Cart

# Create your views here.

def add_to_cart(request):
    if request.method=='POST' and 'pro_id' in request.POST and 'qty' in request.POST and 'demonsion' in request.POST:
        pro_id = request.POST['pro_id']
        qty = request.POST['qty']
        demonsion = request.POST['demonsion']
        if pro_id and qty and demonsion:
            if int(qty)>0:
                cart = Cart(request)
                product = get_object_or_404(Product, pk=pro_id)
                if demonsion=='sm':
                    product.price = product.sm_price
                elif demonsion=='md':
                    product.price = product.md_price
                else:
                    product.price = product.lg_price
                cart.add(product=product, quantity=int(qty), update_quantity=False)
                messages.success(request, 'ce produit a été ajouté au panier avec succès')
            else:
                messages.error(request, 'Veuillez saisir une quantité valide')
        return redirect('/products/' + str(pro_id))
    else:
        return redirect('index')

def remove_from_cart(request,pro_id):
    cart = Cart(request)
    product = get_object_or_404(Product,id=pro_id)
    cart.remove(product)
    return redirect('cart')

def update_cart(request, pro_id):
    if request.method=='POST' and 'new_qty' in request.POST:
        new_qty = request.POST['new_qty']
        if int(new_qty) >0:
            cart = Cart(request)
            product = get_object_or_404(Product, pk=pro_id)
            cart.add(product=product, quantity=int(new_qty), update_quantity=True)
            messages.success(request, 'Votre panier a été modifié avec succès')
        else:
            messages.error(request, 'Veuillez saisir une quantité valide')
    return redirect('cart')

def cart(request):
    cart = Cart(request)
    context = {
        'cart':cart,
        }
    return render(request, 'orders/cart.html', context)

def checkout(request):
    cart = Cart(request)
    if request.method=='POST' and 'btncheckout' in request.POST:
        if 'fname' in request.POST and 'lname' in request.POST and 'phone' in request.POST and 'city' in request.POST:
            fname = request.POST['fname']
            lname = request.POST['lname']
            phone = request.POST['phone']
            city = request.POST['city']
            if fname and lname and phone and city:
                order = Order.objects.create(
                    first_name=fname,
                    last_name=lname,
                    phone=phone,
                    city=city)
                for item in cart:
                    OrderItem.objects.create(
                        order=order,
                        product=item['product'],
                        price=item['price'],
                        quantity=item['quantity'])
                cart.clear()
                return redirect('thanks')
            else:
                messages.error(request, 'veuillez entrer des informations valides! ')
        else:
            messages.error(request, 'vérifier les erreurs! ')
    context = {'cart': cart}
    return render(request, 'orders/checkout.html', context)