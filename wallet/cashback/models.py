from django.db import models

# Create your models here.
class Customer(models.Model):
    document = models.CharField(
        max_length=15,
        help_text="CPF do customer"
    )

    name = models.CharField(
        max_length=100,
        help_text="Nome do customer"
    )

    def __str__(self):
        return f"Customer: ({self.id}){self.name}-{self.document}"
