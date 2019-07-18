
from django.contrib import admin
from django.urls import path , include
from django.views.generic import RedirectView
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
urlpatterns = [
    path('admin/', admin.site.urls),
    path('catloge/',include('catloge.urls')),
    path('',RedirectView.as_view(url='/catloge/' , permanent = True ))
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
