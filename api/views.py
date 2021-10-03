from rest_framework.decorators import permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated,IsAdminUser 
from accounts.models import BankBranche,User,UserBankAccount,Loan
from .serializers import BankBrancheSerializer,BankUserSerializer,UserBankAccountSerializer,LoanSerializer
from rest_framework import viewsets

class BankBrancheViewSet (viewsets.ModelViewSet):
    permission_classes = (IsAdminUser , )
    queryset = BankBranche.objects.all()
    serializer_class = BankBrancheSerializer


class BankUserViewSet (viewsets.ModelViewSet):
    permission_classes = (IsAdminUser , )
    queryset =User.objects.all()
    serializer_class = BankUserSerializer

class UserBankAccountViewSet (viewsets.ModelViewSet):
    permission_classes = (IsAdminUser , )
    queryset = UserBankAccount.objects.all()
    serializer_class = UserBankAccountSerializer


class LoanViewSet (viewsets.ModelViewSet):
    permission_classes = (IsAdminUser , )
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
