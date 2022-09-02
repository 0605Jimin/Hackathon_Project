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
    path('<int:post_pk>/comment/new', views.comment_new, name='comment_new'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<int:pk>/like', views.post_like, name='post_like'),
    path('<int:pk>/unlike', views.post_unlike, name='post_unlike'),

]
