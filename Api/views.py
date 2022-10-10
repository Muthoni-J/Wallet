# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from wallet.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet
from .serializer import AccountSerializer, CardSerializer, CurrencySerializer, CustomerSerializer, LoanSerializer, NotificationSerializer, ReceiptSerializer, RewardSerializer, ThirdpartySerializer, TransctionSerializer, WalletSerializer

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class CurrencyViewset(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class WalletViewset(viewsets.ModelViewSet):
    queryset = Wallet.objects.all()
    serializer_class = WalletSerializer

class AccountViewset(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class CustomerViewset(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    
class TransactionViewset(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransctionSerializer

class CardViewset(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer

class ThirdpartyViewset(viewsets.ModelViewSet):
    queryset = Thirdparty.objects.all()
    serializer_class = ThirdpartySerializer
    
class NotificationViewset(viewsets.ModelViewSet):
    queryset = Notification.objects.all()
    serializer_class = NotificationSerializer  
class  ReceiptViewset(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer
class  LoansViewset(viewsets.ModelViewSet):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
class  RewardViewset(viewsets.ModelViewSet):
    queryset = Reward.objects.all()
    serializer_class = RewardSerializer    