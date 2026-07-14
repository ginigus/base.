from django.db import models

class Customer(models.Model):
    name = models.CharField(max_length=100, verbose_name="ФИО")
    city = models.CharField(max_length=50, blank=True, null=True, verbose_name="Город")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата регистрации")

    class Meta:
        db_table = 'customers'  # Связываем с твоей таблицей в MySQL

    def __str__(self):
        return self.name

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название товара")
    category = models.CharField(max_length=50, verbose_name="Категория")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена")

    class Meta:
        db_table = 'products'

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
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        db_column='customer_id', 
        verbose_name="Клиент"
    )
    order_date = models.DateField(verbose_name="Дата заказа")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Статус")

    class Meta:
        db_table = 'orders'

    def __str__(self):
        return f"Заказ №{self.id} ({self.get_status_display()})"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, db_column='order_id')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, db_column='product_id')
    qty = models.IntegerField(verbose_name="Количество")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена на момент покупки")

    class Meta:
        db_table = 'order_items'
        unique_together = (('order', 'product'),)