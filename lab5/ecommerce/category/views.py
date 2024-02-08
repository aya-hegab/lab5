from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from category.models import Category
from .forms import *
from django.contrib.auth.decorators import login_required
# from django.views import View


@login_required()
def categoryUpdate(request, cid):
  obj1 = Category.objects.get(id=cid)
  context={'category':obj1}
  if request.method == "POST":
    if request.POST['cname'] != "":
      obj = Category.objects.filter(id=cid)[0]
      obj.name = request.POST['cname'] 
      obj.img = request.FILES['cimg']
      obj.save()
      r=reverse('categories')    
      return HttpResponseRedirect(r)
    else:
      context={'errMsg':"all are required"}
  return render(request, 'category/categoryUpdate.html', context)

# class categoryUpdate(View):
#   def get(self, request, id):
#     context={'category':CategoryForm(instance=Category.objects.get(id=id))}
#     return render(request, 'category/categoryUpdate.html', context)
#   def post(self, request, id):
#       obj = Category.objects.filter(id=id)[0]
#       obj.name = request.POST['name'] 
#       obj.img = request.FILES['img']
#       obj.save()
#       r=reverse('categories')    
#       return HttpResponseRedirect(r)

def categoryList(request):
  context={'categories':Category.objects.all()}
  return render(request, 'category/index.html', context)

# @login_required()
# def categoryAddNew(request):
#   if request.method == "POST":
#     Category.objects.create(name=request.POST['cname'], img=request.FILES['cimg']) 
#     r=reverse('categories')    
#     return HttpResponseRedirect(r)
#   return render(request, 'category/categoryAdd.html')
@login_required()
def categoryAddNewForm(request):
  form = CategoryForm()
  context = {"form": form}
  if request.method == "POST":
    form=CategoryForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      r=reverse('categories')    
      return HttpResponseRedirect(r)
  return render(request, 'category/categoryAddForm.html',context)

@login_required()
def categoryDetails(request, cid):
  obj1 = Category.objects.get(id=cid)
  context={'category':obj1}
  return render(request, 'category/categoryDetails.html', context)

@login_required()
def categoryDelete(request, cid):
  Category.objects.get(id=cid).delete()
  return HttpResponseRedirect('/categories')


