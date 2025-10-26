
from django.contrib import admin
from django.urls import path

from ar_bank.views import home_view,branch_view,account_types_view,accounts_view,customers_view,employees_view,add_branch_view,add_accounttype_view,edit_branch_view,delete_branch_view,edit_accounttype_view,delete_accounttype_view,add_customer_view,edit_customer_view,delete_customer_view,add_account_view,edit_account_view,delete_account_view,add_employee_view,edit_employee_view,delete_employee_view,add_withdraw_view,edit_withdraw_view,delete_withdraw_view,add_deposit_view,edit_deposit_view,delete_deposit_view,add_transfer_view,edit_transfer_view,delete_transfer_view,add_transaction_view,edit_transaction_view,delete_transaction_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home_page'),
    path('AR branches/',branch_view,name='branch_page'),
    path('account types/',account_types_view,name='account_types_page'),
    path('accounts/',accounts_view,name='accounts_page'),
    path('customers/',customers_view,name='customers_page'),
    path('employess/',employees_view,name='employees_page'),
    
    path('add_branch/',add_branch_view, name="add_branch_page"),
    path('edit branch/<int:branch_id>/',edit_branch_view,name="edit_branch_page"),
    path('delete_branch/<int:branch_id>/',delete_branch_view,name="delete_branch_page"),
    
    path('add account type/',add_accounttype_view,name="add_accounttype_page"),
    path('edit account type/<int:accounttype_id>/',edit_accounttype_view,name="edit_accounttype_page"),
    path('delete account type/<int:accounttype_id>/',delete_accounttype_view,name="delete_accounttype_page"),

    path('add customer/',add_customer_view, name="add_customer_page"),
    path('edit customer/<int:customer_id>/',edit_customer_view,name="edit_customer_page"),
    path('delete customer/<int:customer_id>/',delete_customer_view,name="delete_customer_page"),

    path('add account/',add_account_view, name="add_account_page"),
    path('edit account/<int:account_id>/',edit_account_view,name="edit_account_page"),
    path('delete account/<int:account_id>/',delete_account_view,name="delete_account_page"),

    path('add employee/',add_employee_view, name="add_employee_page"),
    path('edit employee/<int:employee_id>/',edit_employee_view,name="edit_employee_page"),
    path('delete employee/<int:employee_id>/',delete_employee_view,name="delete_employee_page"),

    path('add withdraw/',add_withdraw_view, name="add_withdraw_page"),
    path('edit withdraw/<int:withdraw_id>/',edit_withdraw_view,name="edit_withdraw_page"),
    path('delete withdraw/<int:withdraw_id>/',delete_withdraw_view,name="delete_withdraw_page"),

    path('add deposit/',add_deposit_view, name="add_deposit_page"),
    path('edit deposit/<int:deposit_id>/',edit_deposit_view,name="edit_deposit_page"),
    path('delete deposit/<int:deposit_id>/',delete_deposit_view,name="delete_deposit_page"),

    path('add transfer/',add_transfer_view, name="add_transfer_page"),
    path('edit transfer/<int:transfer_id>/',edit_transfer_view,name="edit_transfer_page"),
    path('delete transfer/<int:transfer_id>/',delete_transfer_view,name="delete_transfer_page"),

    path('add transaction/',add_transaction_view, name="add_transaction_page"),
    path('edit transaction/<int:transaction_id>/',edit_transaction_view,name="edit_transaction_page"),
    path('delete transaction/<int:transaction_id>/',delete_transaction_view,name="delete_transaction_page"),






]
