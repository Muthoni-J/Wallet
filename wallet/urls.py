from atexit import register
from pathlib import Path
from unicodedata import name
from django.urls import path

from .views import  account_profile, card_profile, customer_profile, edit_account, edit_customer, edit_transaction, edit_wallet, list_account, list_card, list_currency, list_customers, list_loan, list_notification, list_receipt, list_reward, list_thirdparty, list_transaction, list_wallet, loan_profile, notification_profile, receipt_profile, register_account, register_card,register_currency, register_customer, register_loan, register_notification, register_receipt, register_reward, register_thirdparty, register_wallet, reward_profile, thirdparty_profile, transaction_profile, wallet_profile

urlpatterns = [
        path("register/",register_customer,name="registration"),
        path("currency/",register_currency,name="currency"),
        path("wallet/",register_wallet,name="wallet"),
        path("account/" ,register_account,name="account"),
        path("card/",register_card,name="card"),
        path("thirdparty/",register_thirdparty,name="thirdparty"),
        path("notification/",register_notification,name="notification"),
        path("receipt/",register_receipt,name="receipt"),
        path("loan/",register_loan,name="loan"),
        path("reward/",register_reward,name="reward"),
           
        path("customers/",list_customers, name="list_customers"),
        path("currencys/",list_currency,name="list-currency"),
        path("wallets/",list_wallet,name="list_wallet"),
        path("accounts/",list_account,name="list_account"),
        path("transactions/",list_transaction,name="list_transaction"),
        path("cards/",list_card,name="list_card"),
        path("thirdpartys/",list_thirdparty,name="list_thirdparty"),
        path("notifications/",list_notification,name="list_notification"),
        path("receipts/",list_receipt,name="list_receipt"),
        path("loans/",list_loan,name="list_loan"),
        path("rewards/",list_reward,name="list_reward"),
        
         
        path("customers/<int:id>/",customer_profile,name ='customer_profile'),
        path("wallets/<int:id>/",wallet_profile,name ='wallet-profile'),
        path("account/<int:id>/",account_profile,name ='account-profile'),
        path("transaction/<int:id>/",transaction_profile,name ='transaction-profile'),
        path("card/<int:id>/",card_profile,name ='card-profile'),
        path("thirdparty/<int:id>/",thirdparty_profile,name ='thirdparty-profile'),
        path("notification/<int:id>/",notification_profile,name ='notification-profile'),
        path("receipt/<int:id>/",receipt_profile,name ='receipt-profile'),
        path("loan/<int:id>/",loan_profile,name ='loan-profile'),
        path("reward/<int:id>/",reward_profile,name ='reward-profile'),
        
        
        path("customers/edit/<int:id>/",edit_customer,name = 'edit-customer'),
        path("wallets/edit/<int:id>/",edit_wallet,name ='edit-wallet'),
        path("accounts/edit/<int:id>/",edit_account,name ='edit-account'),
        path("card/edit/<int:id>/",edit_account,name ='edit-card'),
        path("card/transaction/<int:id>/",edit_transaction,name ='edit-transaction'),

    ]