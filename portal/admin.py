from django.contrib import admin

from portal.models import Registration
from portal.models import Deposit
from portal.models import WithDraw
from portal.models import Transaction

class RegisterInfo(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'bod', 'email','gender','address','city','postal_code','country','password')
    search_fields = ('email', )
class DepositInfo(admin.ModelAdmin):
    list_display = ('account','date','amount')

class WithdrawInfo(admin.ModelAdmin):
    list_display = ('account','date', 'amount')

class TransactionInfo(admin.ModelAdmin):
    list_display = ('account', 'date', 'transaction_type','amount','after_balance')
    search_fields = ('date', )

admin.site.register(Registration, RegisterInfo)
admin.site.register(Deposit,DepositInfo)
admin.site.register(WithDraw, WithdrawInfo)
admin.site.register(Transaction,TransactionInfo)