from django.forms import ModelForm

from ar_bank.models import Branch,Account_type,Customer,Account,Employee,Transaction,Transfer,Withdraw,Deposit

class BranchForm(ModelForm):
    class Meta:
        model = Branch
        fields = '__all__'

class Account_typeForm(ModelForm):
    class Meta:
        model = Account_type
        fields = '__all__'

class Account_typeForm(ModelForm):
    class Meta:
        model = Account_type
        fields = '__all__'

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = '__all__'

class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class WithdrawForm(ModelForm):
    class Meta:
        model = Withdraw
        fields = '__all__'

class DepositForm(ModelForm):
    class Meta:
        model = Deposit
        fields = '__all__'

class TransferForm(ModelForm):
    class Meta:
        model = Transfer
        fields = '__all__'

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = '__all__'