from django.urls import path, include
from rest_framework.routers import DefaultRouter

from Passwords.views import CategoryView, PassViewSet

router = DefaultRouter()
router.register(r'passes', PassViewSet, basename='pass')

urlpatterns = [
    path('category/', CategoryView.as_view(), name='category'),
    path('', include(router.urls)),
]