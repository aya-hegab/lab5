from . import views
from django.urls import path
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.categoryList, name="categories"),
    # path('new', views.categoryAddNew, name="categories.add"),
    path('newform', views.categoryAddNewForm, name="categories.addform"),
    path('<int:cid>', views.categoryDetails, name='categories.details'),
    path('delete/<int:cid>', views.categoryDelete, name='categories.delete'),
    path('update/<cid>', views.categoryUpdate, name='categories.update'),
]