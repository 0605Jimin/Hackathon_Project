from django.urls import path
from . import views
from accounts import views as accounts_views

app_name = 'accounts'  # URL Reverse에서 namespace역할을 함

urlpatterns = [
    path('login/', accounts_views.login, name='login'),
    path('logout/', accounts_views.logout, name='logout'),
    path('signup/', accounts_views.signup, name='signup'),

]
