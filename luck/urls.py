from.import views
from django.urls import path
urlpatterns=[
    path("",views.page,name='page'),
    path("login/",views.login, name='login'),
    path("signup/",views.signup, name='signup'),
    path("dash/",views.dash, name='dash'),
]