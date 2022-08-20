from django.urls import path

from .views import ZepepListCreateAPIView


urlpatterns = [
    path('zepep/', ZepepListCreateAPIView.as_view()),
]
