from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.models import *

class ProductSeria(serializers.Serializer):
  id=serializers.IntegerField(read_only=True)
  name=serializers.CharField(max_length=100)
  img=serializers.ImageField()

  def create(self, validated_data):
    return Product.objects.create(**validated_data)

  def update(self, instance, validated_data):
        instance.name=validated_data.get('name')
        instance.img=validated_data.get('img')
        instance.save()
        return instance


@api_view(['GET'])
def hello(request):
  return Response({'msg':"hello"})

@api_view(['GET'])
def listproductsapi(request):
  data= Product.productList()
  datajson=ProductSeria(data,many=True).data
  return Response({'msg':f"{datajson}"})

@api_view(['GET'])
def productDetailsapi(request,pk):
  data= ProductSeria(Product.productDetails(pk)).data
  return Response({'msg':f"{data}"})

@api_view(['POST'])
def addapi(request):
  obj=ProductSeria(data=request.data)
  if obj.is_valid():

    obj.save()
  return Response({'msg':f"data"})

@api_view(['PUT'])
def update(request, pk):
  productdata = Product.objects.filter(id=pk).first()

  if(productdata):
      serlizeddata=ProductSeria(instance=productdata,data=request.data)
      if serlizeddata.is_valid():
          serlizeddata.save()
          return Response(data=serlizeddata.data,status=200)
  return Response(serlizeddata.errors,status=400)

@api_view(['DELETE'])
def deleteapi(request,id):
    productdata=Product.objects.filter(id=id)
    if(len(productdata)>0):
        productdata.delete()
        return Response(data={'msg':'deleted'})
    return Response({'msg':'product not found'})