@login_required
def dashboard(request):
    # Главная страница со списками
    customers = Customer.objects.all()
    products = Product.objects.all()
    orders = Order.objects.all()
    return render(request, 'dashboard.html', {
        'customers': customers,
        'products': products,
        'orders': orders
    })

@login_required
def edit_product(request, pk=None):
    # Создание или редактирование товара
    product = get_object_or_400(Product, pk=pk) if pk else None
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = ProductForm(instance=product)
    return render(request, 'edit_product.html', {'form': form, 'product': product})

@login_required
def delete_product(request, pk):
    product = get_object_or_400(Product, pk=pk)
    if request.method == 'POST':
        product.delete()
        return redirect('dashboard')
    return render(request, 'confirm_delete.html', {'object': product})