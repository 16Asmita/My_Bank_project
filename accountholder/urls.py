"""
URL configuration for accountholder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from portal import views 

admin.site.site_header = 'BankManagement Admin '
admin.site.index_title = 'BankManagement Information'

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('',views.portal,name="portal" ),
    # path('login/', include('login.urls')),
    path('login/',views.login,name="login" ),
    path('create/',views.login_save,name="login_save" ),
    path('registration/', views.registration,name="registration"),
    path('save/', views.add_register, name="add_register"),
    path('deposit/',views.deposit,name="deposit"),
    path('insert/',views.deposit_save,name="deposit_save"),

    path('withdraw/',views.withdraw,name="withdraw"),
    path('add/',views.withdraw_save,name="withdraw_save"),

    path('transaction/',views.transaction,name="transaction"),
    path('get_data/',views.get_previous_balance,name="get_previous_balance"),
    # path('view/',views.transaction_view,name="transaction_view"),

]

