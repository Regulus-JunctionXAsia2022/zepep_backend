from django.urls import path

from .views import MyZepepListAPIView, ZepepListCreateAPIView, ZepepUpdateAPIView


urlpatterns = [
    path('zepep/', ZepepListCreateAPIView.as_view()),
    path('zepep/<zepep_id>', ZepepUpdateAPIView.as_view()),
    path('zepep/my/', MyZepepListAPIView.as_view()),
]
