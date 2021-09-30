from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('workout/', include('workout.urls')),
    path('', RedirectView.as_view(url='/workout/', permanent=True)),
    path('accounts/', include('django.contrib.auth.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)