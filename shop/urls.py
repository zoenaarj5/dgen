from django.urls import path
from . import views
urlpatterns=[
    path("",views.index, name="index"),
    path("products/",views.listProducts,name="listProducts"),
    path("products/<int:product_id>",views.showProduct,name="showProduct"),
    path("stores/<int:store_id>/products/",views.listStoreProducts,name="listStoreProducts"),
    path("stores/",views.listStores,name="listStores"),
    path("stores/<int:store_id>",views.showStore,name="showStore"),
]