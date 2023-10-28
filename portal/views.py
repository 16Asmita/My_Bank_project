from django.shortcuts import render, redirect
from django.http import HttpResponse
from portal.models import Registration, Deposit,WithDraw,Transaction
from django.contrib import messages
from decimal import Decimal
from django.utils import timezone


def portal(request):
    portals_main = "welcome to our bank"
    portal_body = "\n allows individuals, governments, and corporations to get the necessary \n financial support. It enables you to borrow funds at competitive \n interest rates. It allows borrowers to manage their cash \n flow. It empowers you to initiate instant money transfers and make \n payments remotely."

    return render(request, "portal.html", {
        "portal_main": portals_main,
        "portal_body": portal_body
    })
 
def registration(request):
    return render(request, "registration.html")

def add_register(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        lname = request.POST.get('lastname')
        boddate= request.POST.get('bod')
        email_id = request.POST.get('email')
        if Registration.objects.filter(email=email_id).exists():
            messages.success(request, 'Email Already Exists.')
            return redirect('/registration/')
        else:
            gender_select = request.POST.get('gender')
            user_address = request.POST.get('address')
            user_city = request.POST.get('city')
            code = request.POST.get('postal_code')
            user_country = request.POST.get('country')
            user_password = request.POST.get('password')

            registration = Registration(firstname=fname,lastname=lname,bod=boddate,email=email_id,gender=gender_select,address=user_address,city= user_city,postal_code=code,country=user_country,password= user_password)
            registration.save()

            messages.success(request, "You are registration successfully.... ")
            return redirect('/login/')
    return HttpResponse('404 - Not Records Found')


def login(request):
    return render(request, "login.html")

def login_save(request):
    if request.method == 'POST':
        user_email = request.POST.get('email')  
        user_password = request.POST.get('password')
        login = Registration.objects.filter(email=user_email, password = user_password).first()
        if login is not None:
            email = login.email
            password = user_password
            messages.success(request, 'You are Successfully Login In....')
            return redirect('/deposit/')
        else:
            messages.error(request, 'Your email and password not valid...Please Try Again.')
            return redirect('/login/')  

def deposit(request):
    return render(request, "deposit.html")

def deposit_save(request):
        if request.method == "POST":
            user_account = request.POST.get('account')
            balace = request.POST.get('amount')

            balance = Decimal(balace)

            previous_balance = get_previous_balance(user_account)
            new_balance = previous_balance + balance


            deposit = Deposit(account=user_account, amount=balace)
            deposit.save()

            transaction = Transaction(
                date = timezone.datetime.now(),
                account=user_account,
                transaction_type='Deposit',
                amount=balace,
                after_balance=new_balance
        )
        transaction.save()
        messages.success(request, 'Your Deposit Successfully Added....')

        return redirect('/transaction/')


def withdraw(request):
    return render(request, "withdraw.html")

def withdraw_save(request):
        if request.method == "POST":
            user_account = request.POST.get('account')
            balace = request.POST.get('amount')

            balance = Decimal(balace)

            previous_balance = get_previous_balance(user_account)
            new_balance = previous_balance - balance

            withdraw = WithDraw(account=user_account, amount=balace)
            withdraw.save()


            transaction = Transaction(
                date = timezone.datetime.now(),
                account=user_account,
                transaction_type='Withdraw',
                amount=balace,
                after_balance=new_balance
        )
        transaction.save()
        messages.success(request, 'Your Withdraw Successfully Added....')

        return redirect('/transaction/')


def get_previous_balance(user_account):
    previous_transaction = Transaction.objects.filter(account=user_account).order_by('-date').first()
    
    if previous_transaction:
        return previous_transaction.after_balance
    else:
        return Decimal('0')

def transaction(request):
    transactions = Transaction.objects.order_by('-date')
    return render(request, "transaction.html", {
        "transactions": transactions
    })

