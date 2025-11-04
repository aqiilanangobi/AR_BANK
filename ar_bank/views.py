from django.shortcuts import render,redirect
from django.contrib import messages
#from django.contrib.auth.forms import UserCreationForm

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
    branchs = Branch.objects.all()
    
    if request.method == "POST":
        
        if branch_form.is_valid():
            branch_form.save()
            messages.success(request,"Branch Added Successfully")
            
        else:
            messages.error(request,"Form is invalid...")
    else:
        branch_form = BranchForm()

    
    
    context = {
        'form': branch_form,
        'branchs':branchs
    }

    return render(request,"add_branch.html",context)

def edit_branch_view(request,branch_id):
    branch = Branch.objects.get(id=branch_id)

    if request.method =="POST":
        branch_form = BranchForm(request.POST,instance=branch)
        if branch_form.is_valid():
            branch_form.save()
            messages.success(request,"changes saved successfully") 
            return redirect(add_branch_view)
        else:
            messages.error(request,"Form has invalid data")
    else:
        branch_form = BranchForm(instance=branch)
    
    context = {
        'form': branch_form,
        'branch': branch,
    }

    return render(request,'edit_branch.html',context)

def delete_branch_view(request,branch_id):
    
    branch = Branch.objects.get(id=branch_id)
    branch.delete()
    messages.success(request,"Branch deleted successfully")

    return redirect('/add_branch/')


def add_accounttype_view(request):
   
    accounttypes = Account_type.objects.all()
    
    if request.method == 'POST':
        accounttype_form = Account_typeForm(request.POST)
        if accounttype_form.is_valid():
            accounttype_form.save()
            messages.success(request,"Account type added successfully")
        else:
            messages.error(request,"Form is invalid...")
    else:
        accounttype_form = Account_typeForm()
        
    

    context = {
        'form': accounttype_form,
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
            messages.success(request,"changes saved successfully")
            
            return redirect(add_accounttype_view)
        
        else:
            messages.error("Form has invalid data")
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

    messages.success(request,"Account type deleted successfully ")

    return redirect('/add account type/')


def add_customer_view(request):
   
    customers = Customer.objects.all()
    
    
    if request.method == "POST":
        customer_form = CustomerForm(request.POST)

        if customer_form.is_valid():
           customer_form.save()
           messages.success("Customer added successfully")
           
        else:
            messages.error("form has invalid data")
    else:
        customer_form = CustomerForm()

    
    
    context = {
        'form': customer_form,
        'customers':customers
    }

    return render(request,"add_customer.html",context)

def edit_customer_view(request,customer_id):
    customer =Customer.objects.get(id=customer_id)

    if request.method =="POST":
        customer_form = CustomerForm(request.POST,instance=customer)
        if customer_form.is_valid():
            customer_form.save()
            messages.success("changes saved successfully")
           
            return redirect(add_customer_view)
        else:
            messages.error(request,"Form has invalid data")
    else:
        customer_form = CustomerForm(instance=customer)
    
    context = {
        'form': customer_form,
        'customer': customer,
        
    }

    return render(request,'edit_customer.html',context)

def delete_customer_view(request,customer_id):
    customer =Customer.objects.get(id=customer_id)
    customer.delete()

    messages.success(request,"customer deleted successfully")

    return redirect('/add customer/')


def add_account_view(request):
   
    accounts = Account.objects.all()
    
    if request.method == "POST":
        account_form = AccountForm(request.POST)

        if account_form.is_valid():
           account_form.save()
           message = "account added successfully"
        else:
            print("Form is invalid...")
    else:
        account_form = AccountForm()

    context = {
        'form': account_form,
        'accounts':accounts
    }

    return render(request,"add_account.html",context)

def edit_account_view(request,account_id):

    account = Account.objects.get(id=account_id)

    if request.method =="POST":
        account_form = AccountForm(request.POST,instance=account)
        if account_form.is_valid():
            account_form.save()
            messages.success(request,"changes saved successfully")

            return redirect(add_account_view)
        
        else:
            messages.error(request,"Form has invalid data")
    else:
        account_form = AccountForm(instance=account)
    
    context = {
        'form': account_form,
        'account': account,
    }

    return render(request,'edit_account.html',context)

def delete_account_view(request,account_id):
    account =Account.objects.get(id=account_id)
    account.delete()
    messages.success(request,"Account deleted successfully")

    return redirect('/add account/')

def add_employee_view(request):
    
    employees = Employee.objects.all()
    if request.method == "POST":
        employee_form = EmployeeForm(request.POST)

        if employee_form.is_valid():
           employee_form.save()
           messages.success(request,"employee added successfully")
        else:
            messages.error(request,"Form is invalid...")
    else:
        employee_form = EmployeeForm()

    
    
    context = {
        'form': employee_form,
        'employees':employees
    }

    return render(request,"add_employee.html",context)

def edit_employee_view(request,employee_id):
   
    employee = Employee.objects.get(id=employee_id)

    if request.method =="POST":
        employee_form = EmployeeForm(request.POST,instance=employee)
        if employee_form.is_valid():
            employee_form.save()
            messages.success(request,"changes saved successfully")
            return redirect(add_employee_view)
        
        else:
            messages.error(request,"Form has invalid data")
    else:
        employee_form = EmployeeForm(instance=employee)
    
    context = {
        'form': employee_form,
        'employee': employee,
    }

    return render(request,'edit_employee.html',context)

def delete_employee_view(request,employee_id):
    employee =Employee.objects.get(id=employee_id)
    employee.delete()

    messages.success(request,"Employee deleted successfully")

    return redirect('/add employee/')


def add_withdraw_view(request):
    
    withdraws = Withdraw.objects.all()
    
    if request.method == "POST":
        withdraw_form = WithdrawForm(request.POST)

        if withdraw_form.is_valid():
           withdraw_form.save()
           messages.success(request,"deposit info added successfully")
        else:
            messages.error(request,"Form is invalid...")
    else:
        withdraw_form = WithdrawForm()

    
    context = {
        'form': withdraw_form,
        'withdraws':withdraws
    }

    return render(request,"add_withdraw.html",context)



def edit_withdraw_view(request,withdraw_id):

    withdraw = Withdraw.objects.get(id=withdraw_id)

    if request.method =="POST":
        withdraw_form = WithdrawForm(request.POST,instance=withdraw)
        
        if withdraw_form.is_valid():
            withdraw_form.save()
            messages.success(request,"changes saved successfully")
            return redirect(add_withdraw_view)
        else:
            messages.error(request,"Form has invalid data")
    else:
        withdraw_form = WithdrawForm(instance=withdraw)
    
    context = {
        'form': withdraw_form,
        'withdraw': withdraw,
    }

    return render(request,'edit_withdraw.html',context)

def delete_withdraw_view(request,withdraw_id):
    withdraw =Withdraw.objects.get(id=withdraw_id)
    withdraw.delete()

    messages.success(request,"Withdraw deleted successfully")

    return redirect('/add withdraw/')


def add_deposit_view(request):
    deposits = Deposit.objects.all()
    
    if request.method == "POST":
        deposit_form = DepositForm(request.POST)

        if deposit_form.is_valid():
           deposit_form.save()
           messages.success(request,"deposit info added successfully")
        else:
            messages.error(request,"Form is invalid...")
    else:
        deposit_form = DepositForm()

    
    
    context = {
        'form': deposit_form,
        'deposits':deposits
    }

    return render(request,"add_deposit.html",context)

def edit_deposit_view(request,deposit_id):
    deposit = Deposit.objects.get(id=deposit_id)

    if request.method =="POST":
        deposit_form = DepositForm(request.POST,instance=deposit)
        if deposit_form.is_valid():
            deposit_form.save()
            messages.success(request,"changes saved successfully")
            return redirect(add_deposit_view)
        else:
            messages.error(request,"Form has invalid data")
    else:
        deposit_form = DepositForm(instance=deposit)
    
    context = {
        'form': deposit_form,
        'deposit': deposit,
    }

    return render(request,'edit_deposit.html',context)

def delete_deposit_view(request,deposit_id):
    deposit =Deposit.objects.get(id=deposit_id)
    deposit.delete()

    messages.error(request,"deposit deleted successfully")

    return redirect('/add deposit/')


def add_transfer_view(request):

    transfers = Transfer.objects.all()

    if request.method == "POST":
        transfer_form = TransferForm(request.POST)

        if transfer_form.is_valid():
           transfer_form.save()
           messages.success(request,"transfer info added successfully")
        else:
           messages.error(request,"Form is invalid...")
    else:
        transfer_form = TransferForm()

    
    
    context = {
        'form': transfer_form,
        'transfers':transfers
    }

    return render(request,"add_transfer.html",context)

def edit_transfer_view(request,transfer_id):

    transfer = Transfer.objects.get(id=transfer_id)

    if request.method =="POST":
        transfer_form = TransferForm(request.POST,instance=transfer)
        if transfer_form.is_valid():
            transfer_form.save()
            messages.success(request,"changes saved successfully")
            return redirect(add_transfer_view)
        else:
            messages.error(request,"Form has invalid data")
    else:
        transfer_form = TransferForm(instance=transfer)
    
    context = {
        'form': transfer_form,
        'transfer': transfer,
    }

    return render(request,'edit_transfer.html',context)

def delete_transfer_view(request,transfer_id):
    transfer =Transfer.objects.get(id=transfer_id)
    transfer.delete()

    messages.success(request,"Transferdeleted successfully")

    return redirect('/add transfer/')


def add_transaction_view(request):
   
    transactions = Transaction.objects.all()
    
    
    if request.method == "POST":
        transaction_form = TransactionForm(request.POST)

        if transaction_form.is_valid():
           transaction_form.save()
           messages.success(request,"transaction info added successfully")
        else:
            messages.error(request,"Form is invalid...")

    else:
        transaction_form = TransactionForm()
    

    
    
    context = {
        'form': transaction_form,
        'transactions':transactions
    }

    return render(request,"add_transaction.html",context)

def edit_transaction_view(request,transaction_id):
   
    transaction = Transaction.objects.get(id=transaction_id)

    if request.method =="POST":
        transaction_form = TransactionForm(request.POST,instance=transaction)
        if transaction_form.is_valid():
            transaction_form.save()
            messages.success(request,"changes saved successfully")
            return redirect(add_transaction_view)
        else:
            messages.error(request,"Form has invalid data")
    else:
        transaction_form = TransactionForm(instance=transaction)
    
    context = {
        'form': transaction_form,
        'transaction': transaction,
        
    }

    return render(request,'edit_transaction.html',context)

def delete_transaction_view(request,transaction_id):
    transaction =Transaction.objects.get(id=transaction_id)
    transaction.delete()

    messages.success(request,"Transaction deleted successfully")

    return redirect('/add transaction/')

'''''

def sign_up_view(request):
    message = ''
    if request.method == "POST":
        sign_up_form = UserCreationForm.POST
        if sign_up_form.is_valid():
            sign_up_form.save()
            message ="User created successfully"
        else:
            message = "Something went wrong"
    else:
        sign_up_form =UserCreationForm()
    

    context = {
        'form':sign_up_form,
        'message':message
    }
    return render(request,'registration/sign_up.html',context)
'''














    

                            














    

                            