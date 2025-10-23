from django.shortcuts import render, get_object_or_404
from . import models
from django.views.generic import TemplateView,ListView,DetailView
from cartapp.forms import CartAddProductForm

# Create your views here.
class ProductListView(ListView):
    model= models.Product
    template_name = 'store/product_list.html'

class ProdView(DetailView):
    model= models.Product
    context_object_name = 'prod_dets'
    form_class =  CartAddProductForm
    template_name = 'store/product_dets.html'
    #cart_product_form = CartAddProductForm()
