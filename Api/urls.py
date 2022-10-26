from django.urls import path,include
from rest_framework import routers
from .views import AccountBuy_AirtimeView, AccountDepositView, AccountRepay_loanView, AccountRequest_loanView, AccountTransferView, AccountViewset, AccountWithdrawView, CardViewset, CurrencyViewset, CustomerViewset, LoansViewset, NotificationViewset, ReceiptViewset, RewardViewset, ThirdpartyViewset, TransactionViewset, WalletViewset
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
    path("deposit/", AccountDepositView.as_view(), name="deposit-view"),
    path("transfer/", AccountTransferView.as_view(), name="transfer-view"),
    path("withdraw/", AccountWithdrawView.as_view(), name="withdraw-view"),
    path("request_loan/", AccountRequest_loanView.as_view(), name="withdraw-view"),
    path("repay_loan/", AccountRepay_loanView.as_view(), name="withdraw-view"),
    path("buy_airtime/", AccountBuy_AirtimeView.as_view(), name="withdraw-view"),
]