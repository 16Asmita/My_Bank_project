from django.db import models


class Login(models.Model):
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=20)


    class Meta:
        db_table = "login_info"


class Registration(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    bod = models.CharField(max_length=30)
    email = models.CharField(max_length=100, default=None)
    gender = models.CharField(max_length=20, default=None)
    address = models.CharField(max_length=200, default=None)
    city = models.CharField(max_length=100, default=None)
    postal_code = models.CharField(max_length=20, default=None)
    country = models.CharField(max_length=30, default=None)
    password = models.CharField(max_length=30, default=None)


    class Meta:
        db_table = "register_info"

    
class Transaction(models.Model):
    TRANSACTION_TYPES = (
        ('Deposit', 'Deposit'),
        ('Withdraw', 'Withdraw'),
    )
    # user = models.ForeignKey(Registration,on_delete=models.CASCADE,default=None)
    account = models.CharField(max_length=20,default=None)
    date = models.CharField(max_length=30)
    transaction_type = models.CharField(max_length=50, choices=TRANSACTION_TYPES)
    amount = models.DecimalField(max_digits=30, decimal_places=2,default=None)
    after_balance = models.DecimalField(max_digits=50,decimal_places=2,default=None)

    class Meta:
        db_table = "transaction_info"
        
class Deposit(models.Model):
    account = models.CharField(max_length=30,default=None)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=30, decimal_places=2)

    class Meta:
        db_table = "deposit_info"

class WithDraw(models.Model):
    account = models.CharField(max_length=30,default=None)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.DecimalField(max_digits=30, decimal_places=2)

    class Meta:
        db_table = "withdraw_info"