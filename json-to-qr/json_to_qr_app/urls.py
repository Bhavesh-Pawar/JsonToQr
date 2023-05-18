from django.urls import path
from json_to_qr_app.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',IndexView.as_view(),name='index')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
