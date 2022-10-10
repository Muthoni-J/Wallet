from modulefinder import Module
from re import A
from django.contrib import admin
from .models import Customer,Wallet,Account,Transaction,Card,Thirdparty,Notification,Receipt,Loan,Reward,Currency

# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","email","gender","address","age","nationality","id_number","phone_number","email","employment_status","employment_status")
    search_fields = ("first_name","last_name",) 
admin.site.register(Customer,CustomerAdmin)

class CurrencyAdmin(admin.ModelAdmin):
    list_display = ("country_origin","currency_rate")
    search_fields = ("country_origin","currency_rate",)
admin.site.register(Currency,CurrencyAdmin)
                   
class WalletAdmin(admin.ModelAdmin):
    list_display = ("balance","date","profile","customer","pin","is_active","currency")
    search_fields = ("balance","date",)
admin.site.register(Wallet, WalletAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("wallet","account_type","balance","name")
    search_fields = ("wallet","account_type",)
admin.site.register(Account,AccountAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ("amount","transaction_type","transaction_cost","status","receipt","account_origin","destination","receipt")
    search_fields = ("amount","transaction_type",)
admin.site.register(Transaction,TransactionAdmin)

class CardAdmin(admin.ModelAdmin):
    list_display = ("signature","date_issued","card_status","CVV_security_code","account")
    search_fields = ("signature","date_issued",)
admin.site.register(Card,CardAdmin)

class ThirdpartyAdmin(admin.ModelAdmin):
    list_display = ("email","phone_number","is_active","currency","transaction_cost","account")
    search_fields = ("email","phone_number",)
admin.site.register(Thirdparty,ThirdpartyAdmin)

class NotificationAdmin(admin.ModelAdmin):
    list_display = ("message","data_created","image","receipt","is_active")
    search_fields = ("message","data_created",)
admin.site.register(Notification,NotificationAdmin)

class ReceiptAdmin(admin.ModelAdmin):
    list_display = ("date",)
    search_fields = ("date",)
admin.site.register(Receipt,ReceiptAdmin)

class LoanAdmin(admin.ModelAdmin):
    list_display = ("balance","guaranter","amount","status","duration_in_month","wallet","date_time","interest_rate")
    search_fields = ("balance","guaranter",)
admin.site.register(Loan,LoanAdmin)

class RewardAdmin(admin.ModelAdmin):
     list_display = ("transaction","wallet","name","points","date")
     search_fields = ("transaction","wallet",)
admin.site.register(Reward,ReceiptAdmin)
    
    
