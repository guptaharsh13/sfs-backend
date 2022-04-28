from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from .views import index

admin.site.site_title = 'Secure File Storage'
admin.site.site_header = 'Secure File Storage Admin Panel'
admin.site.index_title = 'Welcome to Secure File Storage Admin Panel'

urlpatterns = [

    path('auth/', include('rest_framework_social_oauth2.urls')),
    path("secure/", include('secure_files.urls')),

    path('admin/', admin.site.urls),
    path('', view=index, name="index"),
    # path('api-auth/', include('rest_framework.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
