from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from chat.free_chat.views import message


urlpatterns = [
    path('', message, name='index'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)