from django.shortcuts import render

from catalog.models import Product


def home(request):
    return render(request, "home.html")


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        message = request.POST.get("message")
        print(name, phone, message)
    return render(request, "contacts.html")


def base_r(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "product_list.html", context)
