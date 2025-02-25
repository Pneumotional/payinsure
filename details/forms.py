from django import forms
from .models import Customer, Product, Referral

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone_number', 'date_of_birth', 'email', 'customer_type']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your phone number'}),
            'date_of_birth': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter your email'}),
            'customer_type': forms.Select(attrs={'class': 'form-control'}),
        }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['usage_type', 'make', 'model', 'manufacturing_year', 'chassis_number', 'vehicle_colour', 'start_date']
        widgets = {
            'usage_type': forms.Select(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter vehicle make'}),
            'model': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter vehicle model'}),
            'manufacturing_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter manufacturing year'}),
            'chassis_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter chassis number'}),
            'vehicle_colour': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter vehicle colour'}),
            'start_date': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'YYYY-MM-DD', 'type': 'date'}),
        }

class ReferralForm(forms.ModelForm):
    class Meta:
        model = Referral
        fields = ['referral_type', 'agent_code']
        widgets = {
            'referral_type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter referral type'}),
            'agent_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter agent code'}),
        }