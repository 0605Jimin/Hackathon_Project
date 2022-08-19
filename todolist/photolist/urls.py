from django.urls import path
from . import views
from django.conf.urls.static import static

app_name = 'photolist'  # URL Reverse에서 namespace역할을 함

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('', views.photo_list, name='photo_list'),
    path('<int:pk>', views.photo_detail, name='photo_detail'),
    # path('', views.home, name='home'),
    path('account/', views.account, name='account'),

]
