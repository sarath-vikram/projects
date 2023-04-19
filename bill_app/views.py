from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User,auth
from django.contrib import messages
from bill_app.models import Category,Brand,Supplier,Customer,Product
from django.contrib.auth.decorators import login_required


# Create your views here.

def base(request):
    return render(request,'base.html')

def login(request):
    return render(request,'login.html')


def dologin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username,password=password)
        if user != None:
            auth.login(request,user)
            
            return redirect('admin_home')
            
        else:
            messages.info(request,'Username or Password is wrong')  
            return redirect('login')  
    return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required(login_url='/')
def admin_home(request):
    return render(request,'admin/admin_home.html')

@login_required(login_url='/')
def add_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if Category.objects.filter(name=name).exists():
            messages.info(request,'Category Already Exist')
            return redirect('add_category')
        else:
            category = Category(
                name = name
            )
            category.save()
            messages.info(request,'Category added successfully')
            return redirect('add_category')
    return render(request,'admin/add_category.html')


@login_required(login_url='/')
def view_category(request):
    category = Category.objects.all()
    context = {
        'category':category
    }
    return render(request,'admin/view_category.html',context)


@login_required(login_url='/')
def edit_category(request,id):
    category = Category.objects.get(id=id)
    context = {
        'category':category
    }
    return render(request,'admin/edit_category.html',context)

@login_required(login_url='/')
def update_category(request):
    if request.method == 'POST':
        name = request.POST.get('name')  
        category_id = request.POST.get('category_id')

        category = Category.objects.get(id=category_id)
        if Category.objects.filter(name=name).exists():
            messages.info(request,'Category Already Exist')
            return redirect('update_category')
        else:

            category.name = name
            category.save()
            messages.info(request,'Category updated successfully')
            return redirect('view_category')
    return render(request,'admin/edit_category.html')

@login_required(login_url='/')
def delete_category(request,id):
    category = Category.objects.get(id=id)
    category.delete()
    messages.info(request,'Category successfully deleted')
    return redirect('view_category')



def add_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')

        if Brand.objects.filter(name=name).exists():
            messages.info(request,'Brand Already Exist')
            return redirect('add_brand')
        else:
            brand = Brand(
                name = name
            )
            brand.save()
            messages.info(request,'Brand added successfully')
            return redirect('add_brand')
    return render(request,'admin/add_brand.html')

@login_required(login_url='/')
def view_brand(request):
    brand = Brand.objects.all()
    context = {
        'brand':brand
    }
    return render(request,'admin/view_brand.html',context)


@login_required(login_url='/')
def edit_brand(request,id):
    brand = Brand.objects.get(id=id)
    context = {
        'brand':brand
    }
    return render(request,'admin/edit_brand.html',context)


@login_required(login_url='/')
def update_brand(request):
    if request.method == 'POST':
        name = request.POST.get('name')  
        brand_id = request.POST.get('brand_id')

        brand = Brand.objects.get(id=brand_id)
        if Brand.objects.filter(name=name).exists():
            messages.info(request,'Brand Already Exist')
            return redirect('update_brand')
        else:

            brand.name = name
            brand.save()
            messages.info(request,'Brand updated successfully')
            return redirect('view_brand')
    return render(request,'admin/edit_brand.html')


@login_required(login_url='/')
def delete_brand(request,id):
    brand = Brand.objects.get(id=id)
    brand.delete()
    messages.info(request,'Brand successfully deleted')
    return redirect('view_brand')




@login_required(login_url='/')
def add_supplier(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_sup = request.POST.get('mobile_sup')
        if Supplier.objects.filter(name=name).exists():
            messages.info(request,'Supplier Already Exist')
            return redirect('add_supplier')
        else:
            supplier = Supplier(
                name = name,
                mobile_sup = mobile_sup
            )
            supplier.save()
            messages.info(request,'Supplier added successfully')
            return redirect('add_supplier')
    return render(request,'admin/add_supplier.html')


@login_required(login_url='/')
def view_supplier(request):
    supplier = Supplier.objects.all()
    context = {
        'supplier':supplier
    }
    return render(request,'admin/view_supplier.html',context)

@login_required(login_url='/')
def edit_supplier(request,id):
    supplier = Supplier.objects.get(id=id)
    context = {
        'supplier':supplier
    }
    return render(request,'admin/edit_supplier.html',context)

@login_required(login_url='/')
def update_supplier(request):
    if request.method == 'POST':
        supplier_id = request.POST.get('supplier_id')
        name = request.POST.get('name')
        mobile_sup = request.POST.get('mobile_sup')

        supplier = Supplier.objects.get(id=supplier_id)
        supplier.name = name
        supplier.mobile_sup = mobile_sup
        supplier.save()
        messages.info(request,'Supplier updated Successfully')
        return redirect('view_supplier')
    return render(request,'admin/edit_supplier.html')


@login_required(login_url='/')
def delete_supplier(request,id):
    supplier = Supplier.objects.get(id=id)
    supplier.delete()
    messages.info(request,'Supplier successfully deleted')
    return redirect('view_supplier')

@login_required(login_url='/')
def add_product(request):
    category = Category.objects.all()
    brand = Brand.objects.all()
    supplier = Supplier.objects.all()

    if request.method == 'POST':
        name = request.POST.get('name')
        unique_id = request.POST.get('unique_id')
        category_id = request.POST.get('category_id')
        brand_id = request.POST.get('brand_id')
        supplier_id = request.POST.get('supplier_id')
        
        receive_quantity = request.POST.get('receive_quantity')

        if Product.objects.filter(unique_id=unique_id).exists():
            messages.info(request,'Product ID taken')
            return redirect('add_product')
        
        else:
            category = Category.objects.get(id=category_id)
            brand = Brand.objects.get(id=brand_id)
            supplier = Supplier.objects.get(id=supplier_id)
            product = Product(
                name = name,
                unique_id = unique_id,
                category_id = category,
                brand_id = brand,
                supplier_id = supplier,
                receive_quantity = receive_quantity
            )

            product.save()
            messages.info(request,'Product successfully saved')
            return redirect('add_product')
        
            

    context = {
        'category':category,
        'brand':brand,
        'supplier':supplier
    }
    return render(request,'admin/add_product.html',context)


def view_product(request):
    category = Category.objects.all()
    product = Product.objects.all()

    CATID = request.GET.get('category')
    if CATID:
        product = Product.objects.filter(category_id=CATID)
    else:
        product = Product.objects.all()    

    context = {
        'product':product,
        'category':category
    }
    return render(request,'admin/view_product.html',context)