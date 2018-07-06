from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField(default=0,error_messages={
                                'required':'thieeu gia roi',
                                'blank':"sai rui ban oi",
                                'no such table':'ko co bang ghi nao ca'}
                                
                                )
    
    def __str__(self):
        return self.name
    
