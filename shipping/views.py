from django.shortcuts import render, get_object_or_404, redirect
from .forms import ShippingForm, GantiTarifForm, TambahCategoryForm
from .models import Shipping, Category, TarifPerKilo
from datetime import datetime, timedelta, time, date


def all_data(request):
    shipping = Shipping.objects.all().order_by('-id')
    return render(request, 'shipping/home.html', {'shipping': shipping})


def category(request):
    category = Category.objects.all()
    return render(request, 'shipping/category.html', {'category': category})


def ganti_category(request):
    form = TambahCategoryForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('category')

    context = {
        'form': form,

    }

    return render(request, 'shipping/ganti_category.html', context)


def home(request):
    today = datetime.today()
    harian = Shipping.objects.filter(date=today).order_by('-id')

    return render(request, 'shipping/harian.html', {'harian': harian, })


def create(request):
    shipping_form = ShippingForm(request.POST)
    kategori = Category.objects.all()
    harga = TarifPerKilo.objects.all().last()
    tarif = harga.harga
    tarif_per_kilo = int(tarif)

    if request.method == 'POST':
        if shipping_form.is_valid():
            shipping_form.save()

        return redirect('home')

    context = {
        'page_title': 'Tambah shipping',
        'shipping_form': shipping_form,
        'kategori': kategori,
        'tarif_per_kilo': tarif_per_kilo

    }

    return render(request, 'shipping/create.html', context)


def tarifperkilo(request):
    tarif = TarifPerKilo.objects.all().order_by('-id')

    return render(request, 'shipping/tarif.html', {'tarif': tarif})


def ganti_tarif(request):
    form = GantiTarifForm(request.POST)

    if request.method == 'POST':
        if form.is_valid():
            form.save()

        return redirect('tarif')

    context = {
        'form': form,

    }

    return render(request, 'shipping/ganti_tarif.html', context)


def detail(request, pk):
    shipping = get_object_or_404(Shipping, id=pk)
    context = {
        'title': 'detail data',
        'shipping': shipping,
    }

    return render(request, 'shipping/detail.html', context)
