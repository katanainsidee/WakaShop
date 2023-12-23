from django.shortcuts import render, get_object_or_404
from .models import Product


def main(request):
    clothing = Product.objects.all()
    return render(request, 'main/main.html', {'clothing': clothing})


def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'main/product_detail.html', {'product': product})


def contacts(request):
    return render(request, 'main/contacts.html')


def about(request):
    return render(request, 'main/about_us.html')
