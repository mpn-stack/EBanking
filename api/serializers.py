from django.db.models.base import Model
from accounts.models import BankBranche,User,UserBankAccount,Loan
from rest_framework import serializers

class BankBrancheSerializer (serializers.ModelSerializer):    
    class Meta:
        model = BankBranche
        fields = ('id','name', 'City', 'address')
        #read_only_fields =  ('name', 'City', 'address', )
    
    def create(self, validated_data):
        obj = super().create(validated_data)   
        obj.save()
        return obj

class BankUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id','last_login','is_superuser','first_name','last_name'
            ,'is_staff','is_active','date_joined','email')

class UserBankAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserBankAccount
        fields = ('account_no','gender','birth_date','balance'
            ,'interest_start_date','initial_deposit_date','user','account_type','branche_name')

class LoanSerializer(serializers.ModelSerializer):
    debit_amount = serializers.SerializerMethodField()
    loan_interest = serializers.SerializerMethodField()
    class Meta:
        model = Loan
        fields = ('id','user','loan_amount','loan_interest','number_of_installments','paid_installments','debit_amount')

    def get_debit_amount(self, obj):
        total_debt = obj.loan_amount+(obj.loan_amount*20/100)
        if obj.number_of_installments == '12':
            number_of_installments = 12
        else : 
            number_of_installments = 24
        amount_per_month = total_debt / number_of_installments
        if obj.paid_installments == 0 :
            paid_amount = 0
        else :
            paid_amount =  obj.paid_installments * amount_per_month
        # and return appropriate result
        return total_debt-paid_amount
    
    def get_loan_interest(self, obj):
        return obj.loan_amount*20/100