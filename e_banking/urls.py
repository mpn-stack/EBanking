"""e_banking URL Configuration
"""
from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from core.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('admin/', admin.site.urls),
    path('transactions/',include('transactions.urls', namespace='transactions')),
    path('api/', include('api.router')),
    path('api-token-auth/', views.obtain_auth_token)
]