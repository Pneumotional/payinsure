from django.conf import settings
import requests

class PayStack:
    PAYSTACK_SECRET_KEY = 'pk_test_f588bab0f69aa8eb788199a5f07b131c19c7cca1'
    base_url = 'https://api.paystack.co'
    
    def verify_payment(self, ref, *args, **kwargs):
        path = f'/transaction/verify/{ref}'
        
        headers = {
            "Authorization": f"Bearer {self.PAYSTACK_SECRET_KEY}",
            "Content-Type":'application/json'
        }
        url = self.base_url + path
        response = requests.get(url, headers=headers)
        
        if response.status_code == 200:
            response_data = response.json()
            return response_data['status'], response_data['data']
        response_data = response.json()
        return response_data['status'], response_data['message']
        
        
        