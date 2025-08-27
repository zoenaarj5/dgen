import logging
from django.shortcuts import render,get_object_or_404, redirect
from .models import Store,Product,ProductInStore
from django.db import DatabaseError, transaction, IntegrityError
from django.contrib import messages
from .forms import ProductForm, StoreCreationForm,StoreEditForm

logger = logging.getLogger(__name__) #app level logger

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
    title = "Liste des stocks"
    return render(request,"shop/store-list.html",{
        "storez":storeList,
        "title":title
    }) 

def listStoreProducts(request, store_id):
    store = get_object_or_404(Store,id=store_id)
    productzInStore = ProductInStore.objects.filter(store_id=store_id)
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

def editProduct(request,product_id):
    product = get_object_or_404(Product,id=product_id)
    if request.method == "POST":
        productForm = ProductForm(request.POST)
        if(productForm.is_valid()):
            with transaction.atomic():
                product = productForm.save()
                return redirect("showProduct",product_id=product.id)
    else:
        productForm = ProductForm(instance=product)
    
    return render(request,
        "shop/edit-product.html",{
            "product_form":productForm
        })

def addProductSuccess(request,product_id):
    product = get_object_or_404(Product, id=product_id)
    title = f"Le produit \"{str(product.name)}\" a été ajouté."
    return render(request, "shop/add-product-success.html",{
        "product":  product,
        "title" :   title
    })

def addStore(request):
    pageTitle="Créer un stock (un par fédération)"
    if(request.method=="POST"):
        storeForm=StoreCreationForm(request.POST)
        if(storeForm.is_valid()):
            try:
                with transaction.atomic():
                    newStore = storeForm.save()
                    return redirect(f"/shop/show-store/{newStore.id}")

            except IntegrityError as ie:
                logger.warning("Integrity error while saving store",exc_info=ie)
                messages.error(request,"Un stock existe déjà pour le même pays.")

            except DatabaseError as dbe:
                logger.error("Database error while saving store",exc_info=dbe)
                messages.error(request, "Erreur de base de données inattendue.")

            except Exception as e:
                logger.exception("Unexpected error while saving store")
                messages.error(request,"Une erreur est survenue durant l'enregistrement. L'équipe technique est prévenue.")
        else:
            messages.error(request,"Veuillez corriger les erreurs dans ce formulaire.")
    else:
        storeForm=StoreCreationForm()
        return render(request,"shop/add-store.html",{
            "storeForm" : storeForm,
            "title":pageTitle,                                              
        })

def editStore(request,store_id):
    store = get_object_or_404(Store,id=store_id)
    pageTitle="Modifier un stock"
    if(request.method=="POST"):
        storeForm=StoreEditForm(request.POST,instance=store)
        if(storeForm.is_valid()):
            with transaction.atomic():
                updatedStore = storeForm.save()
                updatedStore.save()
                return redirect(f"/shop/show-store/{updatedStore.id}")
    else:
        storeForm=StoreEditForm(instance=store)
        return render(request,"shop/edit-store.html",{
            "storeForm" : storeForm,
            "title":pageTitle,                                              
        })
