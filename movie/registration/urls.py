from django.urls import path
from . import views

app_name = 'register'
urlpatterns = [
    path('',views.login, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.logout, name="logout"),
    path('editprofile',views.editprofile,name="editprofile"),
    path('success/<str:username>', views.success,name="success")


    
]
