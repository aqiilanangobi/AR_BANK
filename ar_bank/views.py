from django.shortcuts import render,redirect

from ar_bank.forms import BranchForm,Account_typeForm,CustomerForm,AccountForm,EmployeeForm,WithdrawForm,DepositForm,TransferForm,TransactionForm
from ar_bank.models import Branch,Account_type,Customer,Account,Employee,Withdraw,Deposit,Transfer,Transaction

def home_view(request):
    return render(request,'home.html')

def branch_view(request):
    return render(request,'branch.html')

def account_types_view(request):
    return render(request,'account_types.html')

def accounts_view(request):
    return render(request,'accounts.html')

def customers_view(request):
    return render(request,'customers.html')

def employees_view(request):
    return render(request,'employees.html')



def add_branch_view(request):
    message = ''
    branch_form = BranchForm(request.POST)
    
    if request.method == "POST":
        branch_form = BranchForm(request.POST)
        if branch_form.is_valid():
            branch_form.save()
            message = "Branch added successfully"
        else:
            print("Form is invalid...")

    branchs = Branch.objects.all()
    
    context = {
        'form': branch_form,
        'msg': message,
        'branchs':branchs
    }

    return render(request,"add_branch.html",context)

def edit_branch_view(request,branch_id):
    message = ''
    branch = Branch.objects.get(id=branch_id)

    if request.method =="POST":
        branch_form = BranchForm(request.POST,instance=branch)
        if branch_form.is_valid():
            branch_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        branch_form = BranchForm(instance=branch)
    
    context = {
        'form': branch_form,
        'branch': branch,
        'message': message
    }

    return render(request,'edit_branch.html',context)

def delete_branch_view(request,branch_id):
    branch = Branch.objects.get(id=branch_id)
    branch.delete()

    return redirect('/add_branch/')




def add_accounttype_view(request):
    message = ''
    accounttype_form = Account_typeForm()

    if request.method == 'POST':
        accounttype_form = Account_typeForm(request.POST)
        if accounttype_form.is_valid():
            accounttype_form.save()
            message = "Account type added successfully"
        else:
            print("Form is invalid...") 
    
    accounttypes = Account_type.objects.all()

    context = {
        'form': accounttype_form,
        'msg': message,
        'accounttypes': accounttypes
    }

    return render(request,"add_accounttype.html",context)

def edit_accounttype_view(request,accounttype_id):
    message = ''
    accounttype =Account_type.objects.get(id=accounttype_id)

    if request.method =="POST":
        accounttype_form = Account_typeForm(request.POST,instance=accounttype)
        if accounttype_form.is_valid():
            accounttype_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        accounttype_form = Account_typeForm(instance=accounttype)
    
    context = {
        'form': accounttype_form,
        'accounttype': accounttype,
        'message': message
    }

    return render(request,'edit_accounttype.html',context)

def delete_accounttype_view(request,accounttype_id):
    accounttype =Account_type.objects.get(id=accounttype_id)
    accounttype.delete()

    return redirect('/add account type/')


def add_customer_view(request):
    message = ''
    customer_form = CustomerForm(request.POST)
    
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
           customer_form.save()
           message = "Customer added successfully"
        else:
            print("Form is invalid...")

    customers = Customer.objects.all()
    
    context = {
        'form': customer_form,
        'msg': message,
        'customers':customers
    }

    return render(request,"add_customer.html",context)

def edit_customer_view(request,customer_id):
    message = ''
    customer =Customer.objects.get(id=customer_id)

    if request.method =="POST":
        customer_form = CustomerForm(request.POST,instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        customer_form = CustomerForm(instance=customer)
    
    context = {
        'form': customer_form,
        'customer': customer,
        'message': message
    }

    return render(request,'edit_customer.html',context)

def delete_customer_view(request,customer_id):
    customer =Customer.objects.get(id=customer_id)
    customer.delete()

    return redirect('/add customer/')


def add_account_view(request):
    message = ''
    account_form = AccountForm(request.POST)
    
    if request.method == "POST":
        account_form = AccountForm(request.POST)

        if account_form.is_valid():
           account_form.save()
           message = "account added successfully"
        else:
            print("Form is invalid...")

    accounts = Account.objects.all()
    
    context = {
        'form': account_form,
        'msg': message,
        'accounts':accounts
    }

    return render(request,"add_account.html",context)

def edit_account_view(request,account_id):
    message = ''
    account = Account.objects.get(id=account_id)

    if request.method =="POST":
        account_form = AccountForm(request.POST,instance=account)
        if account_form.is_valid():
            account_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        account_form = AccountForm(instance=account)
    
    context = {
        'form': account_form,
        'account': account,
        'message': message
    }

    return render(request,'edit_account.html',context)

def delete_account_view(request,account_id):
    account =Account.objects.get(id=account_id)
    account.delete()

    return redirect('/add account/')

def add_employee_view(request):
    message = ''
    employee_form = EmployeeForm(request.POST)
    
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)

        if employee_form.is_valid():
           employee_form.save()
           message = "employee added successfully"
        else:
            print("Form is invalid...")

    employees = Employee.objects.all()
    
    context = {
        'form': employee_form,
        'msg': message,
        'employees':employees
    }

    return render(request,"add_employee.html",context)

def edit_employee_view(request,employee_id):
    message = ''
    employee = Employee.objects.get(id=employee_id)

    if request.method =="POST":
        employee_form = EmployeeForm(request.POST,instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        employee_form = EmployeeForm(instance=employee)
    
    context = {
        'form': employee_form,
        'employee': employee,
        'message': message
    }

    return render(request,'edit_employee.html',context)

def delete_employee_view(request,employee_id):
    employee =Employee.objects.get(id=employee_id)
    employee.delete()

    return redirect('/add employee/')


def add_withdraw_view(request):
    message = ''
    withdraw_form = WithdrawForm(request.POST)
    
    if request.method == "POST":
        withdraw_form = WithdrawForm(request.POST)

        if withdraw_form.is_valid():
           withdraw_form.save()
           message = "deposit info added successfully"
        else:
            print("Form is invalid...")

    withdraws = Withdraw.objects.all()
    
    context = {
        'form': withdraw_form,
        'msg': message,
        'withdraws':withdraws
    }

    return render(request,"add_withdraw.html",context)



def edit_withdraw_view(request,withdraw_id):
    message = ''
    withdraw = Withdraw.objects.get(id=withdraw_id)

    if request.method =="POST":
        withdraw_form = WithdrawForm(request.POST,instance=withdraw)
        
        if withdraw_form.is_valid():
            withdraw_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        withdraw_form = WithdrawForm(instance=withdraw)
    
    context = {
        'form': withdraw_form,
        'withdraw': withdraw,
        'message': message
    }

    return render(request,'edit_withdraw.html',context)

def delete_withdraw_view(request,withdraw_id):
    withdraw =Withdraw.objects.get(id=withdraw_id)
    withdraw.delete()

    return redirect('/add withdraw/')


def add_deposit_view(request):
    message = ''
    deposit_form = DepositForm(request.POST)
    
    if request.method == "POST":
        deposit_form = DepositForm(request.POST)

        if deposit_form.is_valid():
           deposit_form.save()
           message = "deposit info added successfully"
        else:
            print("Form is invalid...")

    deposits = Deposit.objects.all()
    
    context = {
        'form': deposit_form,
        'msg': message,
        'deposits':deposits
    }

    return render(request,"add_deposit.html",context)

def edit_deposit_view(request,deposit_id):
    message = ''
    deposit = Deposit.objects.get(id=deposit_id)

    if request.method =="POST":
        deposit_form = DepositForm(request.POST,instance=deposit)
        if deposit_form.is_valid():
            deposit_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        deposit_form = DepositForm(instance=deposit)
    
    context = {
        'form': deposit_form,
        'deposit': deposit,
        'message': message
    }

    return render(request,'edit_deposit.html',context)

def delete_deposit_view(request,deposit_id):
    deposit =Deposit.objects.get(id=deposit_id)
    deposit.delete()

    return redirect('/add deposit/')


def add_transfer_view(request):
    message = ''
    transfer_form = TransferForm(request.POST)
    
    if request.method == "POST":
        transfer_form = TransferForm(request.POST)

        if transfer_form.is_valid():
           transfer_form.save()
           message = "transfer info added successfully"
        else:
            print("Form is invalid...")

    transfers = Transfer.objects.all()
    
    context = {
        'form': transfer_form,
        'msg': message,
        'transfers':transfers
    }

    return render(request,"add_transfer.html",context)

def edit_transfer_view(request,transfer_id):
    message = ''
    transfer = Transfer.objects.get(id=transfer_id)

    if request.method =="POST":
        transfer_form = TransferForm(request.POST,instance=transfer)
        if transfer_form.is_valid():
            transfer_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        transfer_form = TransferForm(instance=transfer)
    
    context = {
        'form': transfer_form,
        'transfer': transfer,
        'message': message
    }

    return render(request,'edit_transfer.html',context)

def delete_transfer_view(request,transfer_id):
    transfer =Transfer.objects.get(id=transfer_id)
    transfer.delete()

    return redirect('/add transfer/')


def add_transaction_view(request):
    message = ''
    transaction_form = TransactionForm(request.POST)
    
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST)

        if transaction_form.is_valid():
           transaction_form.save()
           message = "transaction info added successfully"
        else:
            print("Form is invalid...")

    transactions = Transaction.objects.all()
    
    context = {
        'form': transaction_form,
        'msg': message,
        'transactions':transactions
    }

    return render(request,"add_transaction.html",context)

def edit_transaction_view(request,transaction_id):
    message = ''
    transaction = Transaction.objects.get(id=transaction_id)

    if request.method =="POST":
        transaction_form = TransactionForm(request.POST,instance=transaction)
        if transaction_form.is_valid():
            transaction_form.save()
            message = "changes saved successfully"
        else:
            message ="Form has invalid data"
    else:
        transaction_form = TransactionForm(instance=transaction)
    
    context = {
        'form': transaction_form,
        'transaction': transaction,
        'message': message
    }

    return render(request,'edit_transaction.html',context)

def delete_transaction_view(request,transaction_id):
    transaction =Transaction.objects.get(id=transaction_id)
    transaction.delete()

    return redirect('/add transaction/')














    

                            














    

                            