from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response

from products.models import Products
from rest_framework.decorators import api_view

from products.serializers import ProductSerializer


# Create your views here.
def hello(request):
    data= Products.objects.all()
    print(data)
    return HttpResponse("Hello, world! This is the products app.")

@api_view(['GET'])
def get_products(request):
    data = Products.objects.all()
    serializeddata = ProductSerializer(data, many=True)
    return Response(serializeddata.data)

@api_view(['GET'])
def get_product(request, id):
    try:
        data = Products.objects.get(pk=id)
        serializeddata = ProductSerializer(data)
        return Response(serializeddata.data)
    except Products.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
