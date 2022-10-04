from atexit import register
from pathlib import Path
from unicodedata import name
from django.urls import path

from .views import Customer_profile, edit_customer, list_account, list_cardt, list_currency, list_customers, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, register_account, register_card,register_currency, register_customers, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_wallet

urlpatterns = [
        path("register/",register_customers,name="registration"),
        path("currency/",register_currency,name="currency"),
        path("wallet/",register_wallet,name="wallet"),
        path("account/" ,register_account,name="account"),
        path("card/",register_card,name="card"),
        path("thirdparty/",register_thirdparty,name="thirdparty"),
        path("notification/",register_notification,name="notification"),
        path("receipt/",register_receipt,name="receipt"),
        path("loan/",register_loan,name="loan"),
        path("reward/",register_reward,name="reward"),
        
        
        
        path("list/",list_customers, name="list_customers"),
        path("currencys/",list_currency,name="list-currency"),
        path("wallets/",list_customers,name="list_wallet"),
        path("accounts/",list_account,name="list_account"),
        path("transactions/",list_transaction,name="list_transaction"),
        path("cards/",list_cardt,name="list_card"),
        path("thirdpartys/",list_thirdparty,name="list_thirdparty"),
        path("notifications/",list_notification,name="list_notification"),
        path("receipts/",list_receipt,name="list_receipt"),
        path("loans/",list_loan,name="list_loan"),
        path("rewards/",list_reward,name="list_reward"),
        
        
        
        
        path("customer/<int:id>/",Customer_profile,name ='customer-profile'),
        path("wallet/<int:id>/",Customer_profile,name ='wallet-profile'),
        path("account/<int:id>/",Customer_profile,name ='account-profile'),
        path("transaction/<int:id>/",Customer_profile,name ='transaction-profile'),
        path("card/<int:id>/",Customer_profile,name ='card-profile'),
        path("thirdparty/<int:id>/",Customer_profile,name ='thirdparty-profile'),
        path("notification/<int:id>/",Customer_profile,name ='notification-profile'),
        path("receipt/<int:id>/",Customer_profile,name ='receipt-profile'),
        path("loan/<int:id>/",Customer_profile,name ='loan-profile'),
        path("reward/<int:id>/",Customer_profile,name ='reward-profile'),
        
        
        path("customer/edit/<int:id>/",edit_customer,name = 'edit-customer'),

    ]