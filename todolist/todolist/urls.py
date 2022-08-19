from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(
        pattern_name = 'photolist:photo_list' 
    ), name='root'),    # url이 빈공간일 때 photolist앱에서 url name인 photo_list로 /photolist 로 감
    path('admin/', admin.site.urls),
    path('photolist/', include('photolist.urls')),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    # static 위치를 알려줌