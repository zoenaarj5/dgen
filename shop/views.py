from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404, redirect
from .models import Store,Product,ProductInStore
from django.db import transaction
from .forms import ProductForm

def index(request):
    return render(request,"shop/home.html",{
        "title":"Welcome home!"
    })

def listProducts(request):
    productList = Product.objects.all()
    title = "Tous les produits"
    return render(request,"shop/product-list.html",{
        "productz":productList,
        "title":title
    })

def showProduct(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    title="Détail du produit \""+product.name+"\""
    return render(request,"shop/product-by-id.html",{
        "product":product,
        "title":title
    })

def listStores(request):
    storeList = Store.objects.all()
    title = "Liste des dépôts"
    return render(request,"shop/store-list.html",{
        "storez":storeList,
        "title":title
    }) 

def listStoreProducts(request, store_id):
    store = get_object_or_404(Store,id=store_id)
    productzInStore = store.productsInStore.all()
    title = "Produits du dépôt "+ store.name + "("+store.federation.name+")"
    return render(request,"shop/products-by-store-id.html",{
        "store":store,
        "productsInStore":productzInStore,
        "title":title
    })

def showStore(request, store_id):
    store = get_object_or_404(Store,id=store_id)
    title = "Détail dépôt "+store.name+"(" + store.federation.name + ")"
    return render(request,"shop/store-by-id.html",{
        "store":store,
        "title":title
    })

def addProduct(request):
    if request.method == "POST":
        productForm = ProductForm(request.POST)
        if(productForm.is_valid()):
            with transaction.atomic():
                product = productForm.save()
                return redirect("addProductSuccess",product_id=product.id)
    else:
        productForm = ProductForm()
    
    return render(request,
        "shop/add-product.html",{
            "product_form":productForm
        })

def addProductSuccess(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    title = f"Le produit \"{str(product.name)}\" a été ajouté."
    return render(request, "shop/add-product-success.html",{
        "product":  product,
        "title" :   title
    })
