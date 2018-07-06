from tastypie.resources import ModelResource
from practice.models import Product
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization


class ProductResources(ModelResource):
    class Meta:
        queryset = Product.objects.all()
#         allowed_methods = ['get']
        resource_name = 'product'
        authorization = Authorization() #error 401
        always_return_data = True