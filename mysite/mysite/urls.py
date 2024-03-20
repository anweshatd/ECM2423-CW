from django.contrib import admin
from django.urls import include,path
from django.views.generic.base import TemplateView

urlpatterns = [
    path("",include("masale.urls")),
    path('admin/', admin.site.urls),
    path("masale/", include("masale.urls")),
    path("accounts/", include("accounts.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
    path("challenges/", include("challenges.urls"))#urls need fixing!
]

from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)