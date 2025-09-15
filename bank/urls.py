"""
URL configuration for bank project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path

from ar_bank.views import home_view,branch_view,account_types_view,accounts_view,customers_view,employees_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home_page'),
    path('AR branches/',branch_view,name='branch_page'),
    path('account types/',account_types_view,name='account_types_page'),
    path('accounts/',accounts_view,name='accounts_page'),
    path('customers/',customers_view,name='customers_page'),
    path('employess/',employees_view,name='employees_page'),
]
