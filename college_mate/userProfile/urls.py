from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentProfileSetUpViewSet

router = DefaultRouter()
router.register(r'profiles', StudentProfileSetUpViewSet)

urlpatterns = [
    path('', include(router.urls)),
]