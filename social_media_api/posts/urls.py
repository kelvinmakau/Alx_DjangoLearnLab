from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PostViewset, CommentViewset

router = DefaultRouter()
router.register(r'posts', PostViewset, basename='post')
router.register(r'comments', CommentViewset, basename='comment')

urlpatterns = [
    path('', include(router.urls))
]