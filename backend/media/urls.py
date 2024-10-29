from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MediaItemViewSet, UserInteractionViewSet

router = DefaultRouter()
router.register(r'media', MediaItemViewSet)
router.register(r'interactions', UserInteractionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
