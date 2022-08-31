from modulefinder import Module
from re import A
from django.contrib import admin
from .models import Customer,Wallet,Account,Transaction,Card,Thirdparty,Notification,Receipt,Loan,Reward,Currency

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email",)
    search_fields = ("first_name","last_name",) 
admin.site.register(Customer,CustomerAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("country_origin","currency_rate",)
admin.site.register(Currency,CurrencyAdmin)
                   
class WalletAdmin(admin.ModelAdmin):
    list_display = ("balance","date",)
    search_fields = ("pin","profile",)
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("wallet","account_type",)
    search_fields = ("balance","name",)
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("amount","transaction_type",)
    search_fields = ("amount","transaction_type",)
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ("signature","date_issued",)
    search_fields = ("card_status","CVV_security_code",)
admin.site.register(Card,CardAdmin)


class ThirdpartyAdmin(admin.ModelAdmin):
     list_display = ("email","phone_number",)
     search_fields = ("is_active","currency",)
admin.site.register(Thirdparty,ThirdpartyAdmin)


class NotificationAdmin(admin.ModelAdmin):
     list_display = ("message","data_created",)
     search_fields = ("image","receipt",)
admin.site.register(Notification,NotificationAdmin)
class ReceiptAdmin(admin.ModelAdmin):
     search_fields = ("receipt_file","transaction",)
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
     list_display = ("balance","guaranter",)
     search_fields = ("amount","status",)
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
     list_display = ("transaction","wallet",)
     search_fields = ("points","date",)
admin.site.register(Reward,ReceiptAdmin)
    
    
