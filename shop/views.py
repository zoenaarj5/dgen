from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Store,Product,ProductInStore

def index(request):
    return HttpResponse("Welcome to our shop !")

def shopHome(request, federation_id):
    return HttpResponse("This is the shopping home page.")

def listProducts(request):
    productList = Product.objects.all()
    title = "Tous les produits"
    return render(request,"product-list.html",{
        "productz":productList,
        "title":title
    })

def showProduct(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    title="Détail du produit \""+product.name+"\""
    return render(request,"product-by-id.html",{
        "product":product,
        "title":title
    })

def listStores(request):
    storeList = Store.objects.all()
    title = "Liste des dépôts"
    return render(request,"store-list.html",{
        "storez":storeList,
        "title":title
    }) 

def listStoreProducts(request, store_id):
    store = get_object_or_404(Store,id=store_id)
    productzInStore = store.productsInStore.all()
    title = "Produits du dépôt "+ store.name + "("+store.federation.name+")"
    return render(request,"products-by-store-id.html",{
        "store":store,
        "productsInStore":productzInStore,
        "title":title
    })

def showStore(request, store_id):
    store = get_object_or_404(Store,id=store_id)
    title = "Détail dépôt "+store.name+"(" + store.federation.name + ")"
    return render(request,"store-by-id.html",{
        "store":store,
        "title":title
    })

