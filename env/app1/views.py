from django.shortcuts import render,redirect


# Create your views here.
from .models import Product
from .forms import ProductForm

def showallproduct(request):
    products=Product.objects.all()
    context={
        'products' : products
    }
    return render(request,'showproducts.html',context)

def productdetail(request,pk):
    eachproduct=Product.objects.get(id=pk)
    context={
        'eachproduct':eachproduct
    }
    
    return render(request,'productdetail.html',context)

def addproduct(request):
    form = ProductForm()

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('showllproduct')
    else:
        form = ProductForm()

    context = {
        "form":form
    }
    return render(request,'addproduct.html',context)

def updateProduct(request,pk):
    product = Product.objects.get(id=pk)

    form = ProductForm(instance=product)

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            return redirect('showllproduct')

    context = {
        "form":form,
        'eachproduct':product
    }

    return render(request, 'updateproduct.html', context)

def deleteproduct(request,pk):
    product=Product.objects.get(id=pk)
    product.delete()
    return redirect('showllproduct')
