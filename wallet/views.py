
from gzip import READ
from profile import Profile
from webbrowser import get
from django.shortcuts import render,redirect

from wallet.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet
from .forms import CustomerRegistrationForm ,CurrencyRegistrationForm,WalletRegistrationForm,AccountRegistrationForm,TransactionRegistrationForm,CardRegistrationForm,ThirdpartyRegistrationForm,NotificationRegistrationForm,ReceiptRegistrationForm,LoanRegistrationForm,RewardRegistrationForm

# reusable for post(save data),get,delete,patch
# Create your views here.
# def register_customers(request):
#     form = CustomerRegistrationForm()
#     return render(request,"wallet/register_customers.html",
#                   {"form":form})

def register_customer(request):
    if request.method == "POST":
        form = CustomerRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CustomerRegistrationForm()
    return render(request, "wallet/register_customer.html",{"form": form}) 

def list_customers(request):
    customers= Customer.objects.all()
    return render(request, "wallet/list_customers.html",{"customers":customers})
 
def customer_profile(request,id):
    customer = Customer.objects.get(id=id)
    return render (request,"wallet/customer_profile.html",{"customer":customer})
 
def edit_customer(request,id):
    customer= Customer.objects.get(id=id)
    if request.method == "Post":
         form=CardRegistrationForm(request.POST,intance=customer)
         if form.is_valid():
            form.save()
         return redirect("customer_profile",id=customer.id)
    else:
         form=CardRegistrationForm()
    return render(request,"wallet/edit_customer.html",
                  {'form':form})    

    

def register_currency(request):
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()
    return render(request, "wallet/register_customer.html",{"form": form}) 

def list_currency(request):
    currencys= Currency.objects.all()
    return render(request, "wallet/list_currency.html",{"currencys":currencys})  

def currency_profile(request,id):
    currency = Currency.objects.get(id=id)
    return render (request,"wallet/currency_profile.html",{"currency":currency})

def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()
    return render(request, "wallet/register_wallet.html",{"form": form}) 

def list_wallet(request):
    wallets= Wallet.objects.all()
    return render(request, "wallet/list_wallet.html",{"wallets":wallets}) 

def wallet_profile(request,id):
    wallet = Wallet.objects.get(id=id)
    return render (request,"wallet/wallet_profile.html",{"wallet":wallet}) 

def edit_wallet(request,id):
    wallet= Wallet.objects.get(id=id)
    if request.method == "Post":
         form=WalletRegistrationForm(request.POST,intance=wallet)
         if form.is_valid():
            form.save()
         return redirect("wallet_profile",id=wallet.id)
    else:
         form=WalletRegistrationForm()
    return render(request,"wallet/edit_wallet.html",
                  {'form':form})    

 
 

def register_account(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountRegistrationForm()
    return render(request, "account/register_wallet.html",{"form": form}) 

def list_account(request):
    accounts= Account.objects.all()
    return render(request, "account/list_account.html",{"accounts":accounts}) 

def account_profile(request,id):
    account = Account.objects.get(id=id)
    return render (request,"wallet/account_profile.html",{"account":account}) 

def edit_account(request,id):
    account= Account.objects.get(id=id)
    if request.method == "Post":
         form=AccountRegistrationForm(request.POST,intance=account)
         if form.is_valid():
            form.save()
         return redirect("account_profile",id=account.id)
    else:
         form=AccountRegistrationForm()
    return render(request,"account/edit_account.html",
                  {'form':form}) 

    
def register_transaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request, "wallet/register_transaction.html",{"form": form}) 

def list_transaction(request):
    transations= Transaction.objects.all()
    return render(request, "wallet/list_transaction.html",{"transactions":transations})  

def transaction_profile(request,id):
    transaction = Transaction.objects.get(id=id)
    return render (request,"wallet/customer_profile.html",{"transaction":transaction}) 

def edit_transaction(request,id):
    transaction= transaction.objects.get(id=id)
    if request.method == "Post":
         form=TransactionRegistrationForm(request.POST,intance=transaction)
         if form.is_valid():
            form.save()
         return redirect("card_profile",id=transaction.id)
    else:
         form=TransactionRegistrationForm()
    return render(request,"card/edit_card.html",
                  {'form':form})    
 

    
def register_card(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CardRegistrationForm()
    return render(request, "wallet/register_card.html",{"form": form}) 

def list_card(request):
    cards= Card.objects.all()
    return render(request, "card/list_card.html",{"cards":cards}) 

def card_profile(request,id):
    card = Card.objects.get(id=id)
    return render (request,"wallet/card_profile.html",{"card":card}) 

def edit_card(request,id):
    card= Card.objects.get(id=id)
    if request.method == "Post":
         form=CurrencyRegistrationForm(request.POST,intance=card)
         if form.is_valid():
            form.save()
         return redirect("card_profile",id=card.id)
    else:
         form=CardRegistrationForm()
    return render(request,"card/edit_card.html",
                  {'form':form})    


    
def register_thirdparty(request):
    if request.method == "POST":
        form = ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThirdpartyRegistrationForm()
    return render(request, "wallet/register_thirdparty.html",{"form": form}) 

def list_thirdparty(request):
    thidpartys = Thirdparty.objects.all()
    return render(request, "thirdparty/list_thirdparty.html",{"thrdpartys":thidpartys})  

def thirdparty_profile(request,id):
    thirdparty = Thirdparty.objects.get(id=id)
    return render (request,"wallet/customer_profile.html",{"thirdparty":thirdparty})  

        

  
def register_notification(request):
    if request.method == "POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NotificationRegistrationForm()
    return render(request, "wallet/register_notification.html",{"form": form}) 

def list_notification(request):
    notification= Notification.objects.all()
    return render(request, "wallet/list_notification.html",{"currency":currency})  
    
def notification_profile(request,id):
    notification = Notification.objects.get(id=id)
    return render (request,"wallet/customer_profile.html",{"notification":notification})   
    

def register_receipt(request):
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReceiptRegistrationForm()
    return render(request, "wallet/register_receipt.html",{"form": form}) 

def list_receipt(request):
    receipt= Receipt.objects.all()
    return render(request, "wallet/list_receipt.html",{"currency":currency})
    
def receipt_profile(request,id):
    receipt = Receipt.objects.get(id=id)
    return render (request,"wallet/customer_profile.html",{"receipt":receipt}) 

  

def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()
    return render(request, "wallet/register_loan.html",{"form": form}) 

def list_loan(request):
    loan = Loan.objects.all()
    return render(request, "wallet/list_loan.html",{"currency":currency})   
    
def loan_profile(request,id):
    loan = Loan.objects.get(id=id)
    return render (request,"wallet/loan_profile.html",{"loan":loan})   
  
    

def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =RewardRegistrationForm()
    return render(request, "wallet/register_reward.html",{"form": form}) 

def list_reward(request):
    rewards = Reward.objects.all()
    return render(request, "wallet/list_reward.html",{"rewards":rewards})   
    
def reward_profile(request,id):
    reward = Reward.objects.get(id=id)
    return render (request,"wallet/reward_profile.html",{"reward":reward})   

def edit_reward(request,id):
    reward = Reward.objects.get(id=id)
    if request.method == "Post":
         form=RewardRegistrationForm(request.POST,intance=reward)
         if form.is_valid():
            form.save()
         return redirect("reward_profile",id=reward.id)
    else:
         form=RewardRegistrationForm()
    return render(request,"reward/edit_reward.html",
                  {'form':form})    



 
