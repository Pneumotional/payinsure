from django.db import models

class Customer(models.Model):
    CUSTOMER_TYPE_CHOICES = [
        ('individual', 'Individual'),
        ('corporate', 'Corporate'),
    ]

    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    date_of_birth = models.DateField()
    email = models.EmailField(unique=True)
    customer_type = models.CharField(max_length=10, choices=CUSTOMER_TYPE_CHOICES)

    def __str__(self):
        return self.name
    

class Product(models.Model):
    PRODUCT_USAGE_TYPE_CHOICES = [
        ('private_individual', 'Private Individual'),
        ('corporate', 'Corporate'),
    ]

    customer = models.OneToOneField(Customer, on_delete=models.CASCADE)
    usage_type = models.CharField(max_length=20, choices=PRODUCT_USAGE_TYPE_CHOICES)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    manufacturing_year = models.PositiveIntegerField()
    chassis_number = models.CharField(max_length=50)
    vehicle_colour = models.CharField(max_length=30)
    start_date = models.DateField()
    total_premium = models.DecimalField(max_digits=10, decimal_places=2)

    def calculate_premium(self):
        if self.usage_type == 'private_individual':
            return 482
        elif self.usage_type == 'corporate':
            return 500
        return 0

    def save(self, *args, **kwargs):
        self.total_premium = self.calculate_premium()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.make} {self.model} ({self.start_date})"
    

class Referral(models.Model):
    product = models.OneToOneField(Product, on_delete=models.CASCADE)
    referral_type = models.CharField(max_length=100)
    agent_code = models.CharField(max_length=50)

    def __str__(self):
        return f"Referral for {self.product}"