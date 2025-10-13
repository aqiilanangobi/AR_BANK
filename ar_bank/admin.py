from django.contrib import admin

# Register your models here.

from .models import Branch,Account_type,Customer,Account,Employee,Transaction,Transfer,Withdraw,Deposit

class BranchAdmin(admin.ModelAdmin):
    list_display =("name","location")
admin.site.register(Branch,BranchAdmin)


class Account_typeAdmin(admin.ModelAdmin):
    list_display = ("name",)
admin.site.register(Account_type,Account_typeAdmin)


class CustomerAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","address","contact")
admin.site.register(Customer,CustomerAdmin)

class AccountAdmin(admin.ModelAdmin):
    list_display = ("opening_date","branch","customer","pin","balance","account_type","account_status")
admin.site.register(Account,AccountAdmin)

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("first_name","last_name","employee_position","city","contact","gender")
admin.site.register(Employee,EmployeeAdmin)


class TransactionAdmin(admin.ModelAdmin):
    list_display = ("date","amount","transaction_type","account","recorded_by")
admin.site.register(Transaction,TransactionAdmin)

class TransferAdmin(admin.ModelAdmin):
    list_display = ("date","account","transfer_amount","receivers_account","recorded_by")
admin.site.register(Transfer,TransferAdmin)

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ("date","account","withdraw_amount","recorded_by")
admin.site.register(Withdraw,WithdrawAdmin)

class DepositAdmin(admin.ModelAdmin):
    list_display = ("date","account","deposit_amount","recorded_by")
admin.site.register(Deposit,DepositAdmin)
