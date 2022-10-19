from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    sor = request.GET.get("sort")

    def sort_phone(parameter):
        phones = Phone.objects.all().order_by(parameter)
        context = {"phones": phones}
        return render(request, 'catalog.html', context)
    if sor == 'name':
        return sort_phone('name')
    elif sor == 'min_price':
        return sort_phone('price')
    elif sor == 'max_price':
        return sort_phone('-price')
    else:
        return sort_phone('id')


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {"phone": phone}
    return render(request, template, context)
