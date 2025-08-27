from django.urls import path
from . import views
urlpatterns=[
    path("",views.index, name="index"),
    path("products/",views.listProducts,name="listProducts"),
    path("products/<int:product_id>",views.showProduct,name="showProduct"),
    path("add-product/",views.addProduct,name="addProduct"),
    path("add-product-success/<int:product_id>",views.addProductSuccess,name="addProductSuccess"),
    path("edit-product/<int:product_id>",views.editProduct,name="editProduct"),
    path("stores/<int:store_id>/products/",views.listStoreProducts,name="listStoreProducts"),
    path("stores/",views.listStores,name="listStores"),
    path("add-store/",views.addStore,name="addStore"),
    path("edit-store/<int:store_id>",views.editStore,name="editStore"),
    path("show-store/<int:store_id>",views.showStore,name="showStore"),
]