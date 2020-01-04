from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from upload.views import image_upload
urlpatterns = [
    path("", image_upload, name="upload"),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls),
]
print("settings.DEBUG ",settings.DEBUG)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    print("set with debug",urlpatterns)
