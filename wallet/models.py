from django.db import models
from django.utils import timezone


# Create your models here.
class Currency(models.Model):
    country_origin=models.CharField(max_length=25,null=True)  
    currency_rate=models.IntegerField()
    
class Customer(models.Model):
        first_name = models.CharField(max_length =15,null=True)
        last_name = models.CharField(max_length =15,null=True)
        gender = models.CharField(max_length =1,null=True)
        address = models.TextField()
        age = models.PositiveSmallIntegerField()
        nationality = models.CharField(max_length =20,null=True)
        id_number = models.CharField(max_length =10,null=True)
        phone_number = models.CharField(max_length =15,null=True)
        email = models.EmailField()
        employment_status = models.BooleanField(default= False)
        signature = models.ImageField(upload_to='profile/',null=True)
        employment_status = models.BooleanField(default=False)

class Wallet(models.Model):
        balance = models.IntegerField()
        date = models.DateTimeField(default=timezone.now)
        is_active = models.BooleanField(default=False)
        currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Wallet_currency')
        profile = models.ImageField(upload_to='profile/',null=True)
        customer = models.ForeignKey('Customer',on_delete=models.CASCADE,related_name='Wallet_customer')
        pin = models.SmallIntegerField()
        type =models.CharField(max_length=15,null=True)
        
        
class Account(models.Model):
        wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Account_wallet')
        account_type = models.CharField(max_length=15,null=True)
        balance = models.IntegerField()
        name = models.CharField(max_length=50,null=True)
        
           
class Transaction (models.Model):
        amount = models.IntegerField()
        transaction_type = models.CharField(max_length=15,null=True)
        transaction_charge = models.CharField(max_length=5,null=True)
        transaction_cost = models.PositiveIntegerField()
        third_party = models.ForeignKey('Thirdparty',on_delete=models.CASCADE,related_name='Transaction_thirdparty')
        status = models.CharField(max_length=15,null=True)
        account_origin =  models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_account_origin')
        destination = models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Transaction_destination')
        receipt = models.CharField(max_length=20,null=True)
             
class Card(models.Model):
        date_issued = models.DateTimeField(default=timezone.now)
        CVV_security_code = models.PositiveSmallIntegerField()
        signature = models.ImageField(upload_to='profile/',null=True)
        card_status = models.CharField(max_length=100,null=True)
        account = models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Card_Account')
        
class Thirdparty(models.Model):
        email = models.EmailField()
        phone_number = models.CharField(max_length=10,null=True)
        transaction_cost = models.IntegerField()
        currency = models.ForeignKey('Currency',on_delete=models.CASCADE,related_name='Thirdparty_currency')
        account = models.ForeignKey('Account',on_delete=models.CASCADE,related_name='Thirdparty_account')
        is_active = models.BooleanField(default=False)
        
class Notification(models.Model):
        message = models.CharField(max_length=200,null=True)
        data_created = models.DateTimeField(default=timezone.now)
        is_active = models. BooleanField(default=False)
        receipt =  models.ForeignKey('Receipt',on_delete=models.CASCADE,related_name='Notification_receipt')
        image = models.ImageField(upload_to='profile/',null=True)
        
class Receipt(models.Model):
        receipt = models.DateTimeField(default=timezone.now)
        transaction = models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Reciept_transaction')
        file = models.FileField()
        date = models.DateTimeField(default=timezone.now)
        receipt_file = models.FileField()
    
class Loan (models.Model):
        amount = models.PositiveIntegerField()
        duration_in_month = models.CharField(max_length=12,null=True)
        status = models.CharField(max_length=40,null=True)
        wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Loan_wallet')
        date_time = models.DateTimeField(default=timezone.now)
        interest_rate = models.IntegerField()
        balance = models.IntegerField()
        guaranter = models.CharField(max_length=15,null=True)
        
class Reward (models.Model):    
        wallet = models.ForeignKey('Wallet',on_delete=models.CASCADE,related_name='Reward_wallet')
        name = models.CharField(max_length=15,null=True)
        points = models.IntegerField()
        date = models.DateTimeField(default=timezone.now)
        transation = models.ForeignKey('Transaction',on_delete=models.CASCADE,related_name='Reward_transaction')