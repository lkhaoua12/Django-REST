from django.http import JsonResponse
import json
from products.models import Product
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.sereliaziers import ProductSerializer

@api_view(['GET'])
def api_rs(request):
    seriliazer = ProductSerializer(data=request.data)
    if seriliazer.is_valid(raise_exception=True):
        #instance = seriliazer.save()
        #print(instance)
        return Response(seriliazer.data)
