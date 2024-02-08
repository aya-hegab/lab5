from django import forms
from django.core.exceptions import ValidationError
from products.models import Product
from category.models import *

class ProductForm(forms.ModelForm):
  class Meta:
    model=Product
    fields=['name', 'img', 'category']
  # name=forms.CharField(max_length=100, required=True  )
  # category=forms.ChoiceField(choices=Category.getCategory())
  # img=forms.ImageField(required=True)

  # def clean_name(self):
  #   inputName = self.cleaned_data["name"]
  #   obj = Product.objects.filter(name=inputName).exist()
  #   if obj:
  #     raise ValidationError("name exists")
  #   else:
  #     return True;

