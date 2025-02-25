from django.urls import path
from .views import insurance_form

urlpatterns = [
    path('', insurance_form, name='insurance_form'),
    # Add other URL patterns here
]