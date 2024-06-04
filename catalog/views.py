from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView

from catalog.models import Product, Blog


# Create your views here.

# def home(request):
#     return render(request, 'home.html')
#
# def contacts(request):
#     return render(request, 'contacts.html')


class ProductListView(ListView):
    model = Product


class ProductDetailView(DetailView):
    model = Product
