from django.shortcuts import render, redirect,get_object_or_404
from .models import *
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate

def login_user(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("index")
        else:
            messages.info(request, "Username or Password is incorrect")
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    return redirect('signup')

def signup(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"Account was created for {username}")
            return redirect("login")
    context = {'form': form}
    return render(request, 'signup.html', context)

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()
    total_orders = orders.count()
    delivered_orders = orders.filter(status="Delivered").count()
    pending_orders = orders.filter(status="Pending").count()
    context = {'orders': orders, 'customers': customers, 'total_orders': total_orders,
               'delivered_orders': delivered_orders, 'pending_orders': pending_orders}
    return render(request, 'dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

def delete_order(request, id):
    Order.objects.filter(id=id).delete()
    return redirect("your_orders")

def index(request):
    products = Product.objects.all().order_by('id')[:3]
    return render(request, "index.html", {'products': products})

def place_order(request, product_id):
    if request.method == 'POST':
        product = get_object_or_404(Product, id=product_id)
        customer = get_object_or_404(Customer, user_id=request.user.id)
        order = Order(product=product, customer=customer, status="Pending", note="Order is processing")
        order.save()
        messages.success(request, f'Order for product {product.name} placed successfully!')
    return redirect("index")

def your_orders(request):
    customer = get_object_or_404(Customer, user_id=request.user.id)
    orders = Order.objects.filter(customer_id=customer.id).values()
    orders_list = []
    for order in orders:
        product = get_object_or_404(Product, id=order["product_id"])
        orders_list.append({
            "product_name": product.name,
            "name": customer.name,
            "status": order["status"],
            "note": order["note"],
            "id": order["id"],
            "date": order["date_created"],
        })
    return render(request, "your_orders.html", {'orders': orders_list})


def user(request):
    customer = get_object_or_404(Customer, user_id=request.user.id)
    if request.method == 'POST':
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        customer.name = name
        customer.phone = phone
        customer.save()
    customer = get_object_or_404(Customer, user_id=request.user.id)
    return render(request, 'user.html', {"user": customer})
