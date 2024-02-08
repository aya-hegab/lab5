from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from products.models import Product
from .forms import *
from django.views.generic import UpdateView, DetailView, DeleteView, ListView, CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required


class productUpdateGeneric(UpdateView):
  model = Product
  template_name= 'products/productUpdate.html'
  form_class=ProductForm
  context_object_name='form'
  success_url=reverse_lazy("products")

# @login_required()
class productAddNewFormGeneric(CreateView):
  model = Product
  template_name= 'products/productAddForm.html'
  form_class=ProductForm
  context_object_name='form'
  success_url=reverse_lazy("products")

class productDetailsGeneric(DetailView):
  model = Product
  template_name= 'products/productDetails.html'
  context_object_name='product'

class productListGeneric(ListView):
  model = Product
  template_name= 'products/index.html'
  context_object_name='products'

class productDeleteGeneric(DeleteView):
  model = Product
  template_name= 'products/productDelete.html'
  context_object_name='product'
  success_url=reverse_lazy("products")


