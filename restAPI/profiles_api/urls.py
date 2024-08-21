from django.urls import path, include
from .views import HelloAPIView, UserProfileViewset

from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', UserProfileViewset)

urlpatterns = [
    path('hello-view', HelloAPIView.as_view(), name= 'hello_view'),
    path('', include(router.urls))
]
