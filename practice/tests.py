from django.test import TestCase
from practice.models import Product


# Create your tests here.
class ProductTestCase(TestCase):
    def setUp(self):
        Product.objects.create(name="ABCDEF",price=23)
        
        
        