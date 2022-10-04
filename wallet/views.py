from crypt import methods
from locale import currency
from profile import Profile
from webbrowser import get
from django.shortcuts import render,redirect

from wallet.models import Currency, Customer
from .forms import CustomerRegistrationForm ,CurrencyRegistrationForm,WalletRegistrationForm,AccountRegistrationForm,TransactionRegistrationForm,CardRegistrationForm,ThirdpartyRegistrationForm,NotificationRegistrationForm,ReceiptRegistrationForm,LoanRegistrationForm,RewardRegistrationForm

# reusable for post(save data),get,delete,patch
# Create your views here.
def register_customers(request):
    form = CustomerRegistrationForm()
    return render(request,"wallet/register_customers.html",
                  {"form":form})

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
 
def Customer_profile(request,id):
    customers = Customer.objects.get(id=id)
    return render (request,"wallet/customer_profile.html",{"customers":customers})
 



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
    form = CurrencyRegistrationForm()
    return render(request,"wallet/register_wallet.html",
                  {"form":form})
    

def register_currency(request):
    if request.method == "POST":
        form = CurrencyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CurrencyRegistrationForm()
    return render(request, "wallet/register_customer.html",{"form": form}) 

def list_currency(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_currency.html",{"currency":currency})  
    
    

# def register_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/register_customers.html",{"customers":customers})



# def register_wallet(request):
#     form = WalletRegistrationForm()
#     return render(request,"wallet/register_wallet.html",
#                   {"form":form})





# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})


def register_wallet(request):
    if request.method == "POST":
        form = WalletRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = WalletRegistrationForm()
    return render(request, "wallet/register_wallet.html",{"form": form}) 

def list_wallet(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_wallet.html",{"currency":currency})  
 
def register_account(request):
    form = AccountRegistrationForm()
    return render(request,"wallet/register_account.html",
                  {"form":form})
def register_account(request):
    if request.method == "POST":
        form = AccountRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = AccountRegistrationForm()
    return render(request, "account/register_wallet.html",{"form": form}) 

def list_account(request):
    currency= Currency.objects.all()
    return render(request, "account/list_account.html",{"currency":currency})  

# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})

# def edit_customer(request,id):
#     customer= Customer.objects.get(id=id)
#     if request.method == "Post":
#          form=CardRegistrationForm(request.POST,intance=customer)
#          if form.is_valid():
#             form.save()
#          return redirect("customer_profile",id=customer.id)
#     else:
#          form=CardRegistrationForm()
#     return render(request,"wallet/edit_customer.html",
#                   {'form':form}) 
    
    

def register_transaction(request):
    form = TransactionRegistrationForm()
    return render(request,"wallet/register_transaction.html",
                  {"form":form})
    
def register_transaction(request):
    if request.method == "POST":
        form = TransactionRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = TransactionRegistrationForm()
    return render(request, "wallet/register_transaction.html",{"form": form}) 

def list_transaction(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_transaction.html",{"currency":currency})  

    
    
    
    

# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})

# def edit_customer(request,id):
#     customer= Customer.objects.get(id=id)
#     if request.method == "Post":
#          form=CardRegistrationForm(request.POST,intance=customer)
#          if form.is_valid():
#             form.save()
#          return redirect("customer_profile",id=customer.id)
#     else:
#          form=CardRegistrationForm()
#     return render(request,"wallet/edit_customer.html",
#                   {'form':form}) 

def register_card(request):
    form = CardRegistrationForm()
    return render(request,"wallet/register_card.html",
                  {"form":form})
    
def register_card(request):
    if request.method == "POST":
        form = CardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = CardRegistrationForm()
    return render(request, "wallet/register_card.html",{"form": form}) 

def list_cardt(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_card.html",{"currency":currency})  

    
    

# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})

# def edit_customer(request,id):
#     customer= Customer.objects.get(id=id)
#     if request.method == "Post":
#          form=CardRegistrationForm(request.POST,intance=customer)
#          if form.is_valid():
#             form.save()
#          return redirect("customer_profile",id=customer.id)
#     else:
#          form=CardRegistrationForm()
#     return render(request,"wallet/edit_customer.html",
#                   {'form':form}) 
    
    
    
    


def register_thirdparty(request):
    form = ThirdpartyRegistrationForm()
    return render(request,"wallet/register_thirdparty.html",
                  {"form":form})
    
def register_thirdparty(request):
    if request.method == "POST":
        form = ThirdpartyRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ThirdpartyRegistrationForm()
    return render(request, "wallet/register_thirdparty.html",{"form": form}) 

def list_thirdparty(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_thirdparty.html",{"currency":currency})  

    
    

# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})

# def edit_customer(request,id):
#     customer= Customer.objects.get(id=id)
#     if request.method == "Post":
#          form=CardRegistrationForm(request.POST,intance=customer)
#          if form.is_valid():
#             form.save()
#          return redirect("customer_profile",id=customer.id)
#     else:
#          form=CardRegistrationForm()
#     return render(request,"wallet/edit_customer.html",
#                   {'form':form}) 
    
    
    
    
def register_notification(request):
    form = NotificationRegistrationForm()
    return render(request,"wallet/register_notification.html",
                  {"form":form})
  
def register_notification(request):
    if request.method == "POST":
        form = NotificationRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = NotificationRegistrationForm()
    return render(request, "wallet/register_notification.html",{"form": form}) 

def list_notification(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_notification.html",{"currency":currency})  
    
    

# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})

# def edit_customer(request,id):
#     customer= Customer.objects.get(id=id)
#     if request.method == "Post":
#          form=CardRegistrationForm(request.POST,intance=customer)
#          if form.is_valid():
#             form.save()
#          return redirect("customer_profile",id=customer.id)
#     else:
#          form=CardRegistrationForm()
#     return render(request,"wallet/edit_customer.html",
#                   {'form':form}) 
    
    
    
    
def register_receipt(request):
    form = ReceiptRegistrationForm()
    return render(request,"wallet/register_receipt.html",
                  {"form":form})
def register_receipt(request):
    if request.method == "POST":
        form = ReceiptRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReceiptRegistrationForm()
    return render(request, "wallet/register_receipt.html",{"form": form}) 

def list_receipt(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_receipt.html",{"currency":currency})
    
    

# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})

# def edit_customer(request,id):
#     customer= Customer.objects.get(id=id)
#     if request.method == "Post":
#          form=CardRegistrationForm(request.POST,intance=customer)
#          if form.is_valid():
#             form.save()
#          return redirect("customer_profile",id=customer.id)
#     else:
#          form=CardRegistrationForm()
#     return render(request,"wallet/edit_customer.html",
#                   {'form':form}) 
    
    
    
    
    
def register_loan(request):
    form = LoanRegistrationForm()
    return render(request,"wallet/register_loan.html",
                  {"form":form})

def register_loan(request):
    if request.method == "POST":
        form = LoanRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = LoanRegistrationForm()
    return render(request, "wallet/register_loan.html",{"form": form}) 

def list_loan(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_loan.html",{"currency":currency})   
    
    

# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})

# def edit_customer(request,id):
#     customer= Customer.objects.get(id=id)
#     if request.method == "Post":
#          form=CardRegistrationForm(request.POST,intance=customer)
#          if form.is_valid():
#             form.save()
#          return redirect("customer_profile",id=customer.id)
#     else:
#          form=CardRegistrationForm()
#     return render(request,"wallet/edit_customer.html",
#                   {'form':form}) 
    
    
    
    
    
def register_reward(request):
    form = RewardRegistrationForm()
    return render(request,"wallet/register_reward.html",
                  {"form":form})
def register_reward(request):
    if request.method == "POST":
        form = RewardRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form =RewardRegistrationForm()
    return render(request, "wallet/register_reward.html",{"form": form}) 

def list_reward(request):
    currency= Currency.objects.all()
    return render(request, "wallet/list_reward.html",{"currency":currency})   
    
    

# def list_customers(request):
#     customers= Customer.objects.all()
#     return render(request, "wallet/list_customers.html",{"customers":customers})

# def edit_customer(request,id):
#     customer= Customer.objects.get(id=id)
#     if request.method == "Post":
#          form=CardRegistrationForm(request.POST,intance=customer)
#          if form.is_valid():
#             form.save()
#          return redirect("customer_profile",id=customer.id)
#     else:
#          form=CardRegistrationForm()
#     return render(request,"wallet/edit_customer.html",
#                   {'form':form}) 

 
