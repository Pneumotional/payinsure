
import secrets
from django.db import models
from django.urls import reverse
from details.models import Customer, Product
from .paystack import PayStack

class Payment(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    product = models.OneToOneField(Product, on_delete=models.CASCADE)  # Link to the Product
    amount = models.DecimalField(max_digits=10, decimal_places=2, editable=False)  # Make it non-editable
    email = models.EmailField()
    ref = models.CharField(max_length=100, unique=True, blank=True)
    is_verified = models.BooleanField(default=False)



    def save(self, *args, **kwargs):
        ref = secrets.token_urlsafe(50)
        object_with_similar_ref = Payment.objects.filter(ref=ref)  
        if not object_with_similar_ref:
            self.ref = ref
        if not self.amount:  # Set amount based on the product's total_premium
            self.amount = self.product.total_premium
        super().save(*args, **kwargs)
    
        
    def calculate_amt(self)->int:
        return self.amount*100
    
    def verify_payment(self):
        paystack = PayStack()
        status,result = paystack.verify_payment(self.ref, self.amount)
        if status:
            if result['amount']/100 == self.amount:
                self.is_verified = True
            self.save()
        if self.is_verified:
            return True
        return False
    
    

    def __str__(self):
        return f"Payment for {self.customer.name} - Amount: {self.amount}"
    
    def get_absolute_url(self):
        return reverse("Payment_detail", kwargs={"ref": self.ref})
