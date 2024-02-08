from . import views
from django.urls import path, include
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('', views.productListGeneric.as_view(), name="products"),
    path('newform', login_required(views.productAddNewFormGeneric.as_view()), name="products.addform"),
    path('<pk>', views.productDetailsGeneric.as_view(), name='products.details'),
    path('delete/<pk>', views.productDeleteGeneric.as_view(), name='products.delete'),
    path('update/<pk>', views.productUpdateGeneric.as_view(), name='products.update'),
    path('API/', include('products.api.urls')),
    
]
