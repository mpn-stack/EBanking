from django.urls import path

from . import views

app_name = 'api'

urlpatterns = [
    path("BankBranche/", views.BankBrancheViewSet,name="BankBranche"),
    #path("Bank/", views.Bank,name="Bank"),

]
