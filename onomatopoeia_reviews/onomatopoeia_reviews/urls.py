from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth.views import LoginView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('movies/', include('reviews.urls')),
    path('api/', include('reviews.api_urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('login/', LoginView.as_view(template_name='login.html')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
