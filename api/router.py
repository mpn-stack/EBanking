from django.urls import path
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()
router.register('BankBranche',views.BankBrancheViewSet,basename='BankBranche')
router.register('Users',views.BankUserViewSet,basename='Users')
router.register('BankAccount',views.UserBankAccountViewSet,basename='BankAccount')
router.register('Loan',views.LoanViewSet,basename='Loan')


urlpatterns = [
]
urlpatterns += router.urls

