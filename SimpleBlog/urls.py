
from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('registration/', include('registration.urls')),
    path('profiles/', include('profiles.urls')),
    path('blog/', include('blog.urls')),
    path('contact/', include('contact.urls'))
]


urlpatterns += staticfiles_urlpatterns()