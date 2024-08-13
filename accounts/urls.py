from django.urls import path

from .views import SignUpView, LogOutView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("logout/", LogOutView.as_view(), name="logout"),
]
