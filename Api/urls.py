from django.urls import path,include
from rest_framework import routers
from .views import AccountViewset, CardViewset, CurrencyViewset, CustomerViewset, LoansViewset, NotificationViewset, ReceiptViewset, RewardViewset, ThirdpartyViewset, TransactionViewset, WalletViewset
router=routers.DefaultRouter()
router.register(r"customers", CustomerViewset)
router.register(r"currencies", CurrencyViewset)
router.register(r"wallets", WalletViewset)
router.register(r"accounts", AccountViewset)
router.register(r"transactions", TransactionViewset)
router.register(r"cards", CardViewset)
router.register(r"thirdparties", ThirdpartyViewset)
router.register(r"notifications", NotificationViewset)
router.register(r"receipts", ReceiptViewset)
router.register(r"loans", LoansViewset)
router.register(r"rewards", RewardViewset)

urlpatterns=[
    path("",include(router.urls)),
    
]