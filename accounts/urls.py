
from django.urls import include, path

from accounts.views import home,FormTest,logout,logIn

app_name = 'accounts'

urlpatterns = [
    path('', home, name='home'),
    path('formtest/',FormTest.as_view(), name='formtest'),
    path('logout', logout, name='logout'),
    path('login/', logIn, name='login'),

]