from django import forms
from .models import Book , Students, Address, Students2, Address2, GalleryImage

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'price', 'edition']
        
class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ['name', 'age', 'address']  

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']
        
        
class Students2Form(forms.ModelForm):
    addresses = forms.ModelMultipleChoiceField(
        queryset=Address2.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Students2
        fields = ['name', 'age', 'addresses']
        
        
class GalleryImageForm(forms.ModelForm):
    class Meta:
        model = GalleryImage
        fields = ['title', 'image']
