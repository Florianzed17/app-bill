from django.contrib import admin
from django.urls import path, include
from events.views import *
from authentification.views import *
from events.urls import *
from authentification.urls import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('events.urls', namespace='events')),
    path('', include(('authentification.urls', 'authentification'), namespace='authentification')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
