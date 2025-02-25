from django.shortcuts import render, redirect, get_object_or_404
from .forms import PaymentForm
from .models import Customer, Product, Payment
from django.contrib import messages
from .models import Payment


def initiate_payment(request, customer_id):
    # Fetch the customer and their associated product
    customer = get_object_or_404(Customer, id=customer_id)
    product = get_object_or_404(Product, customer=customer)  # Assuming one product per customer

    if request.method == 'POST':
        # payment_form = PaymentForm(request.POST)
        payment = Payment(customer=customer, product=product)
        # payment = payment_form.save(commit=False)  # Don't save yet
        payment.customer = customer  # Associate payment with the customer
        payment.product = product  # Associate payment with the product
        payment.amount = product.total_premium  # Set amount from product's total premium
        payment.email = customer.email  # Set email from customer
        payment.save()  # Now save the payment instance

            # Redirect to the payment processing page (e.g., Paystack)
        public_key = 'pk_test_f588bab0f69aa8eb788199a5f07b131c19c7cca1'
        context = {'payment': payment, 'paystack_public_key': public_key}
        return render(request, 'payment/make_payment.html', context)

    else:
        # payment_form = PaymentForm()
        pass

    return render(request, 'payment/initiate_payment.html')



def verify_payment(request, ref: str):
    # Retrieve the payment object based on the reference
    payment = get_object_or_404(Payment, ref=ref)

    # Verify the payment
    verified = payment.verify_payment()  # Assuming this method exists in your Payment model

    # Provide user feedback based on the verification result
    if verified:
        messages.success(request, 'Payment verification successful!')
        # You may want to update the payment status or perform other actions here
    else:
        messages.error(request, 'Payment verification unsuccessful. Please try again.')

    # Redirect to the initiate payment page or any other relevant page
    return redirect('insurance_form')  # Ensure this matches your URL configuration