from django.shortcuts import render,redirect
from .forms import ProductForm,RegisterForm
from .models import Product
from django.contrib.auth.models import User
from  django.contrib.auth import login,logout,authenticate
from django.contrib.auth.decorators import login_required,user_passes_test
from django.core.paginator import Paginator
from django.db.models import Q
from django.db.models import Sum, F, DecimalField


def admin_required(user):
    return user.is_staff


#home view
@login_required
def home_view(request):

    total_products = Product.objects.count()

    low_stock = Product.objects.filter(
        quantity__gt=0,
        quantity__lte=5
    ).count()

    out_of_stock = Product.objects.filter(
        quantity=0
    ).count()

    inventory_value = Product.objects.aggregate(
        total=Sum(
            F('price') * F('quantity'),
            output_field=DecimalField()
        )
    )['total'] or 0

    context = {
        'total_products': total_products,
        'low_stock': low_stock,
        'out_of_stock': out_of_stock,
        'inventory_value': inventory_value,
    }

    return render(
        request,
        'invApp/home.html',
        context
    )

#create view
@login_required
@user_passes_test(admin_required)
def product_create_view(request):
    form=ProductForm()
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request,'invApp/product_form.html',{'form':form})

#read view
@login_required
def product_list_view(request):
    
    search=request.GET.get('search','')
    stock = request.GET.get('stock', '')
    products = Product.objects.all()
    
    if search:
        products=Product.objects.filter(
            Q(name__icontains=search) |
            Q(sku__icontains=search)
        )
    if stock == 'low':
        products = products.filter(
            quantity__gt=0,
            quantity__lte=5
        )

    elif stock == 'out':
        products = products.filter(
            quantity=0
        )
        
    
    paginator=Paginator(products,5)
    page_num=request.GET.get('page')
    page_obj=paginator.get_page(page_num)
    
    return render(request,'invApp/product_list.html',{'page_obj':page_obj,'search':search,'stock': stock,})

#update view
@login_required
@user_passes_test(admin_required)
def product_update_view(request,product_id):
    product=Product.objects.get(product_id=product_id)
    form=ProductForm(instance=product)
    if request.method=="POST":
        form=ProductForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    return render(request,'invApp/product_form.html',{'form':form})
    
#delete view
@login_required
@user_passes_test(admin_required)
def product_delete_view(request,product_id):
    product=Product.objects.get(product_id=product_id)
    if request.method=='POST':
        product.delete()
        return redirect('product_list')
   
    context={'product':product}
    return render(request,'invApp/product_confirm_delete.html',context)
    

def register_view(request):
    if request.method=="POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user=User.objects.create_user(username=username,password=password)
            login(request,user)
            return redirect('home')
    else:
        form=RegisterForm()
    return render(request,'accounts/register.html',{'form':form})

def login_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return render(request,'accounts/login.html',{'error':'invalid credentials'})
        
    else:
        return render(request,'accounts/login.html')

def logout_view(request):
    if request.method=="POST":
        logout(request)
        return redirect('login')
    else:
        return render(request,'accounts/logout.html')