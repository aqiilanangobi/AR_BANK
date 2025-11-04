from django.db import models

# Create your models here.

class Branch(models.Model):
    name = models.CharField(max_length=50,verbose_name="Branch Name")
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.name}"
    

class Account_type(models.Model):
    name = models.CharField(max_length=50,verbose_name="Account type ")
    
    def __str__(self):
        return f"{self.name}"
        
    
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    address = models.CharField(max_length=100,null=True,blank=True,default="N/A")
    contact = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Account(models.Model):
    ACCOUNT_STATUS = [
        ("A","Active"),
        ("I","Inactive"),
        ("S","Suspended"),
    ]
    opening_date = models.DateField(auto_now=True)
    account_number = models.CharField(max_length=30,default='0000')
    pin = models.CharField(max_length=20)
    balance = models.IntegerField()
    branch = models.ForeignKey(Branch,on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer,on_delete=models.CASCADE)
    account_type = models.ForeignKey(Account_type,on_delete=models.CASCADE)
    account_status = models.CharField(max_length=2,choices = ACCOUNT_STATUS)

    def __str__(self):
        return f"{self.customer} Account"


class Employee(models.Model):
    GENDER = [
        ("F","Female"),
        ("M","Male"),
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    employee_position = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    contact = models.CharField(max_length=10)
    gender =models.CharField(max_length=2,choices=GENDER)

    def __str__(self):
        return f"{self.first_name} {self.employee_position}"

class Transaction(models.Model):
    TRANSACTION =[
        ("D","Deposit"),
        ("W","Withdraw"),
        ("T","Transfer"),
    ]
    date = models.DateField(auto_now=False)
    amount= models.IntegerField(verbose_name="transaction_amount")
    transaction_type = models.CharField(max_length=2,choices=TRANSACTION)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    recorded_by = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account} transaction"

class Transfer(models.Model):
    date = models.DateField(auto_now=False)
    account = models.ForeignKey(Account,on_delete=models.CASCADE,related_name='sent_transfers')
    transfer_amount = models.IntegerField()
    receivers_account = models.ForeignKey(Account,on_delete=models.CASCADE,default='0000',related_name='received_transfers')
    recorded_by = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account} transfer"

class Withdraw(models.Model):
    date = models.DateField(auto_now=False)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    withdraw_amount = models.IntegerField()
    recorded_by = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account} Withdraw"

class Deposit(models.Model):
    date = models.DateField(auto_now=False)
    account = models.ForeignKey(Account,on_delete=models.CASCADE)
    deposit_amount = models.IntegerField()
    recorded_by = models.ForeignKey(Employee,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.account} Deposit"



