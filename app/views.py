from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from app.models import Product, Ingredient
from app.forms import SearchForm
from django.db.models import Q


def index(request):

    return render(request, 'index.html')

def productpage(request):

    contex = dict()
    contex['product'] = Product.objects.all()

    return render(request, 'products.html', contex)

def productdetail(request, id):

    p = get_object_or_404(Product, id=id)

    product1 = Ingredient.objects.filter(product_id=p.pk, rate__gte=0, rate__lte=3)
    product2 = Ingredient.objects.filter(product_id=p.pk, rate__gte=4, rate__lte=7)
    product3 = Ingredient.objects.filter(product_id=p.pk, rate__gte=8, rate__lte=10)

    context = {
        'product1': product1,
        'product2': product2,
        'product3': product3,
        'p': p,
    }

    return render(request, 'product-detail.html', context)

def ingredient(request):
    product1 = Ingredient.objects.filter(rate__gte=0, rate__lte=3)
    product2 = Ingredient.objects.filter(rate__gte=4, rate__lte=7)
    product3 = Ingredient.objects.filter(rate__gte=8, rate__lte=10)

    product1 = Ingredient.objects.raw(
        "select id,name,rate from app_ingredient where rate between 0 and 3 group by name ")
    product2 = Ingredient.objects.raw(
        "select id,name,rate from app_ingredient where rate between 4 and 7 group by name ")
    product3 = Ingredient.objects.raw(
        "select id,name,rate from app_ingredient where rate between 8 and 10 group by name ")

    context = {
        'product1': product1,
        'product2': product2,
        'product3': product3,
    }


    return render(request, 'ingredients.html', context)

def aboutus(request):

    return render(request, 'about-us.html')

def searchresult(request):

    context = dict()
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data[ 'search_query' ]
            context['products'] = Product.objects.filter(
                Q(brand__icontains=search_query) |
                Q(pname__icontains=search_query)
            ).distinct()
            return render(request, 'search-result.html', context)
    return HttpResponseRedirect('/')

