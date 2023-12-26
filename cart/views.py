from django.shortcuts import render, redirect, get_object_or_404
from .models import Cart
from main.models import Product


def view_cart(request):
    # Получаем корзину текущего пользователя
    user_cart = Cart.objects.filter(user=request.user)

    context = {
        'cart': user_cart,
    }

    return render(request, 'cart/view_cart.html', context)


def add_to_cart(request, product_id):
    # Логика добавления товара в корзину
    product = get_object_or_404(Product, id=product_id)
    user_cart, created = Cart.objects.get_or_create(user=request.user, product=product)

    # Если товар уже был в корзине, увеличиваем его количество на 1
    if not created:
        user_cart.quantity += 1
        user_cart.save()

    return redirect('view_cart')


def update_cart(request, cart_id):
    # Логика изменения количества товаров в корзине
    cart_item = get_object_or_404(Cart, id=cart_id)

    if request.method == 'POST':
        new_quantity = int(request.POST['quantity'])
        cart_item.quantity = new_quantity
        cart_item.save()

    return redirect('view_cart')


def remove_from_cart(request, cart_id):
    # Логика удаления товара из корзины
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.delete()
    return redirect('view_cart')


def increment_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    cart_item.quantity += 1
    cart_item.save()

    return redirect('view_cart')


def decrement_cart(request, cart_id):
    cart_item = get_object_or_404(Cart, id=cart_id)
    if cart_item.quantity > 0:
        cart_item.quantity -= 1
        cart_item.save()
    if cart_item.quantity == 0:
        cart_item.delete()
        return redirect('view_cart')
    return redirect('view_cart')
