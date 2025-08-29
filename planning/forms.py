from django import forms
from .models import Event
class EventCreationForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"datetime-local"}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"datetime-local"}))
    vkFieldLabels={
        "title":"Titre",
        "start_date":"Début",
        "end_date":"Fin",
        "intro":"Introduction",
        "content":"Contenu",
        "author":"Auteur",
        "federation":"Fédération"
        
    }
    class Meta:
        model = Event
        fields = [
            "title","start_date","end_date","intro","content","author","federation"
        ]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field,label in self.vkFieldLabels.items():
            self.fields[field].widget.attrs["placeholder"]=label

    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and start >= end:
            raise forms.ValidationError("La date de début de l'événement doit précéder la date de fin.")
        return cleaned_data

class EventEditForm(forms.ModelForm):
    start_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"datetime-local"}))
    end_date = forms.DateTimeField(widget=forms.DateTimeInput(attrs={"type":"datetime-local"}))
    vkFieldLabels={
        "title":"Titre",
        "start_date":"Début",
        "end_date":"Fin",
        "intro":"Introduction",
        "content":"Contenu",
    }
    class Meta:
        model = Event
        fields = [
            "title","start_date","end_date","intro","content"
        ]
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field,label in self.vkFieldLabels.items():
            self.fields[field].widget.attrs["placeholder"]=label
    def clean(self):
        cleaned_data = super().clean()
        start = cleaned_data.get("start_date")
        end = cleaned_data.get("end_date")
        if start and end and start >= end:
            raise forms.ValidationError("La date de début de l'événement doit précéder la date de fin.")
        return cleaned_data