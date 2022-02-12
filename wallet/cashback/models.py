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


class Type(models.Model):
    name = models.CharField(
        max_length=20,
        help_text="Nome do tipo de categoria do produto"
    )
    percentage_cashback = models.FloatField(
        default=5,
        help_text="Porcentagem do cashback (PS: de 0 a 100%)"
    )

    class Meta:
        db_table = "Type"

    def __str__(self):
        return f"Type: ({self.id}) {self.name} - {self.percentage_cashback} %"

class Product(models.Model):
    type = models.ForeignKey(
        Type,
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        help_text="Tipo da categoria dos produtos"
    )
    value = models.FloatField()
    qty = models.IntegerField()
