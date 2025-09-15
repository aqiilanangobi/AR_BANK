from django.shortcuts import render

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
