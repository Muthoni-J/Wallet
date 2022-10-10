from rest_framework import serializers
from wallet.models import Account, Card, Currency, Customer, Loan, Notification, Receipt, Reward, Thirdparty, Transaction, Wallet
class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields =("first_name","last_name","age")
class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields =("country_origin","currency_rate")
class WalletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wallet
        fields =("is_active","date","currency","profile","customer")
class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields =("account_type","balance")
class TransctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields =("amount","transaction_type","transaction_cost","status","account_origin","destination")
class CardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Card
        fields =("date_issued","CVV_security_code","signature","card_status","account")
class ThirdpartySerializer(serializers.ModelSerializer):
    class Meta:
        model = Thirdparty
        fields =("email","phone_number","transaction_cost","is_active","account")
class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Notification
        fields =("message","data_created","receipt","is_active","image")
class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields =("receipt_file","date","receipt","transaction","file")
class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Loan
        fields =("amount","duration_in_month","status","wallet","interest_rate","guaranter","balance")
class RewardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reward
        fields =("name","points","date","transation")                            