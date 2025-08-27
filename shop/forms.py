from django import forms
from .models import Product, Store
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["name","description"]

class StoreCreationForm(forms.ModelForm):
    vkFieldLabels={
        "federation":"Fédération",
        "name":"Nom",
        "description":"Description",
    }
    class Meta:
        model = Store
        fields = ["federation","name","description"]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,label in self.vkFieldLabels.items():
            self.fields[name].widget.attrs["placeholder"]=label

class StoreEditForm(forms.ModelForm):
    vkFieldLabels={
        "federation":"Fédération",
        "name":"Nom",
        "description":"Description",
    }
    class Meta:
        model = Store
        fields = ["federation","name","description"]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for name,label in self.vkFieldLabels.items():
            self.fields[name].widget.attrs["placeholder"]=label