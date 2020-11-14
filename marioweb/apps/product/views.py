# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from apps.product.forms import productForm
from apps.product.models import Product 


#Listar
def productIndex(request):
    product = Product.objects.all().order_by('id')
    context = {'products': product}
    return render(request, 'product/index.html', context)
#Agregar
def productAdd(request):
    if request.method == 'POST': #get put delete 
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/product')
    else:
        form = productForm()
    return render(request, 'product/productAdd.html',{'form':form})
#Editar
def productEdit(request,idProduct):
    product = Product.objects.get(id=idProduct)
    if request.method == 'GET':
        form = productForm(instance=product)
    else:
        form = productForm(request.POST,instance=product)
        if form.is_valid():
            form.save()
        return redirect ('/product')
    return render(request, 'product/productAdd.html',{'form':form})

#Eliminar
def productDelete(request,idProduct):
    product = Product.objects.get(id=idProduct)
    if request.method == 'POST':
        product.delete()
        return redirect ('/product')
    return render (request, 'product/productDelete.html', {'product':product})