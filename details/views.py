from django.shortcuts import render, redirect
from .forms import CustomerForm, ProductForm, ReferralForm
from .models import Customer, Product, Referral

def insurance_form(request):
    if request.method == 'POST':
        customer_form = CustomerForm(request.POST)
        product_form = ProductForm(request.POST)
        referral_form = ReferralForm(request.POST)

        if customer_form.is_valid() and product_form.is_valid() and referral_form.is_valid():
            customer = customer_form.save()
            product = product_form.save(commit=False)
            product.customer = customer  # Associate product with the customer
            product.save()

            referral = referral_form.save(commit=False)
            referral.product = product  # Associate referral with the product
            referral.save()

            # Redirect to the payment initiation page
            return redirect('initiate_payment', customer_id=customer.id)  # Redirect to initiate payment

    else:
        customer_form = CustomerForm()
        product_form = ProductForm()
        referral_form = ReferralForm()

    context = {
        'customer_form': customer_form,
        'product_form': product_form,
        'referral_form': referral_form,
    }
    return render(request, 'details/insurance_forms.html', context)