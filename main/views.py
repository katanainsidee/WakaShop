from django.shortcuts import render
from .models import Product


def main(request):
    clothing = Product.objects.all()
    return render(request, 'main/main.html', {'clothing': clothing})

