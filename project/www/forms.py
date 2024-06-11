

from django import forms
from .models import Place,Trip,Favorite

class PlaceForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    photo = forms.ImageField(widget=forms.FileInput(attrs={'placeholder': 'Choose a photo'}))
    discription = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Discription'}))

    class Meta:
        model = Place
        fields = '__all__'


class TripForm(forms.ModelForm):
    name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Name'}))
    price = forms.CharField(max_length=100, widget=forms.NumberInput(attrs={'placeholder': 'Price'}))
    discription = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Discription'}))
    place = forms.ModelChoiceField(queryset=Place.objects.all(), widget=forms.Select(attrs={'placeholder': 'Select a Category'}))

    class Meta:
        model = Trip
        fields = '__all__'


class FavoriteForm(forms.ModelForm):


    class Meta:
        model = Favorite
        fields = '__all__'


