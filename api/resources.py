# from tastypie.resources import ModelResource
from practice.models import Product
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from tastypie.authentication import ApiKeyAuthentication,BasicAuthentication
from tastypie.paginator import Paginator
from .pa1 import PageNumberPaginator
from tastypie.contrib.gis.resources import ModelResource

from tastypie import fields, utils

class ProductResources(ModelResource):
    description = fields.CharField(default="product")
    class Meta:
        queryset = Product.objects.all()
#         allowed_methods = ['get']
        resource_name = 'product'
        authorization = Authorization() #error 401
        always_return_data = True
        # authentication = BasicAuthentication()
        
        paginator_class = PageNumberPaginator
        
        filtering = {
            "name" : "AB",
        }
        
        
        


    