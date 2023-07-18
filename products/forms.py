from django import forms
from .models import CommentaryProduct, Products

class CommentaryProductForm(forms.ModelForm):
    class Meta:
        model = CommentaryProduct
        fields = ['title', 'text']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder': 'Enter your review a title'}),
            'text': forms.Textarea(attrs={'class':'form-control', 'placeholder': 'Write your comments here'}),
        }
class ProductForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = '__all__'