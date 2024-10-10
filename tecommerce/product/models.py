from django.db import models
from client.models import ModelBase

# Create your models here.

class Product(ModelBase):
    description = models.TextField(
        db_column='description',
        null=False
    )

    quantity = models.IntegerField(
        db_column='quantity',
        null=False,
        default=()
    )

    def __str__(self):
        return f'descricao {self.description}, quantidade {self.quantity}'
