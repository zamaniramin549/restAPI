from django.urls import path, include
from .views import (
    HelloAPIView, 
    UserProfileViewset, 
    UserLoginAPIView,
    ProfileFeedItemApiView
    )

from rest_framework import routers

router = routers.DefaultRouter()
router.register('profile', UserProfileViewset)
router.register('feed-item', ProfileFeedItemApiView)

urlpatterns = [
    path('hello-view/', HelloAPIView.as_view(), name= 'hello_view'),
    path('auth/', UserLoginAPIView.as_view()),
    path('', include(router.urls))
]
