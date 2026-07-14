from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Product, Customer, Order
from .forms import ProductForm

# Главная страница (Панель управления)
@login_required
def dashboard(value_request):
    products = Product.objects.all()
    customers = Customer.objects.all()
    orders = Order.objects.all()
    return render(value_request, 'dashboard.html', {
        'products': products,
        'customers': customers,
        'orders': orders
    })

# Добавление товара
@login_required
def add_product(value_request):
    if value_request.method == 'POST':
        form = ProductForm(value_request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm()
    return render(value_request, 'edit_product.html', {'form': form, 'title': 'Добавить новый товар'})

# Редактирование товара
@login_required
def edit_product(value_request, pk):
    product = get_object_or_404(Product, pk=pk)
    if value_request.method == 'POST':
        form = ProductForm(value_request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm(instance=product)
    return render(value_request, 'edit_product.html', {'form': form, 'title': 'Редактировать товар'})

# Удаление товара
@login_required
def delete_product(value_request, pk):
    product = get_object_or_404(Product, pk=pk)
    if value_request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(value_request, 'confirm_delete.html', {'product': product})

# Регистрация
def register(value_request):
    if value_request.method == 'POST':
        form = UserCreationForm(value_request.POST)
        if form.is_valid():
            user = form.save()
            login(value_request, user)
            return redirect('dashboard')
    else:
        form = UserCreationForm()
    return render(value_request, 'auth/register.html', {'form': form})