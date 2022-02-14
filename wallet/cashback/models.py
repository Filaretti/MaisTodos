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


class Purchase(models.Model):
    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        help_text="Customer que fez essa compra"
    )
    total = models.FloatField(
        default=0,
        help_text="Total da minha compra"
    )
    sold_at = models.DateTimeField(
        verbose_name="data de venda",
        help_text="Data que aconteceu a compra"
    )


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
    purchase = models.ForeignKey(
        Purchase,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    total_value = models.FloatField(
        null=True,
        blank=True,
        help_text="Total calculado do value * qty"
    )
    calculated_cashback = models.FloatField(
        null=True,
        blank=True,
        help_text="Total calculado do cashback "
                  "formula: (total_value * (type.percentage_cashback / 100))"
    )
    customer = models.ForeignKey(
        Customer,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
