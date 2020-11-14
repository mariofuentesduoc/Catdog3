from django.urls import path, include
from apps.product.views import productIndex, productAdd, productEdit, productDelete

urlpatterns = [
    
    path('product', productIndex),
    path('addProduct', productAdd),
    path('editProduct/<int:idProduct>',productEdit),
    path('deleteProduct/<int:idProduct>',productDelete)

]