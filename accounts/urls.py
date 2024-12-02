from .views import SignUpView
from django.contrib.auth.views import LogoutView
from django.urls import path

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
]