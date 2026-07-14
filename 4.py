from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название")
    category = models.CharField(max_length=50, verbose_name="Категория")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.00'))], 
        verbose_name="Цена"
    )

    def __str__(self):
        return self.title

class Order(models.Model):
    STATUS_CHOICES = [
        ('new', 'Новый'),
        ('paid', 'Оплачен'),
        ('shipped', 'Доставлен'),
        ('cancelled', 'Отменен'),
    ]
    customer = models.ForeignKey(
        Customer, 
        on_null=True, 
        blank=True, 
        on_delete=models.SET_NULL, 
        verbose_name="Клиент"
    )
    order_date = models.DateField(verbose_name="Дата заказа")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")

    def __str__(self):
        return f"Заказ №{self.id} ({self.status})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.IntegerField(validators=[MinValueValidator(1)], verbose_name="Количество")
    price = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        validators=[MinValueValidator(Decimal('0.00'))], 
        verbose_name="Цена на момент покупки"
    )

    class Meta:
        unique_together = ('order', 'product')