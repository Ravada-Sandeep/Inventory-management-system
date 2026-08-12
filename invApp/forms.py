from django import forms
from .models import Product
from django.contrib.auth.models import User

class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields='__all__'
        widgets={
            'product_id': forms.NumberInput(
                attrs={'placeholder':'e.g. 1','class':'form-control'}),
            'name': forms.TextInput(
                            attrs={'placeholder':'e.g. shirt','class':'form-control'}),
            'sku': forms.TextInput(
                            attrs={'placeholder':'e.g. S12345','class':'form-control'}),
            'price': forms.NumberInput(
                            attrs={'placeholder':'e.g. 19.99','class':'form-control'}),
            'quantity': forms.NumberInput(
                            attrs={'placeholder':'e.g. 10','class':'form-control'}),
            'supplier': forms.TextInput(
                            attrs={'placeholder':'e.g. ABC corp','class':'form-control'}),
        }
        
        
class RegisterForm(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput,label='Confirm Password')
    class Meta:
        model=User
        fields=['username','password','confirm_password']
    def clean(self):
        cleaned_data=super().clean()
        password=cleaned_data.get('password')
        confirm_password=cleaned_data.get('confirm_password')
        if password and confirm_password and password==confirm_password:
            return cleaned_data
        raise forms.ValidationError('password do not match')