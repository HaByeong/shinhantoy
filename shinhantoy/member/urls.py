from django.urls import path, include
from member import views

urlpatterns=[
    path("", views.MemberRegisterView.as_view()),
    path("/password", views.MemberChangePasswordView.as_view()),
]
