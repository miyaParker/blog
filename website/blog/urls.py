from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UsersViewSet, PostsViewSet

app_name = 'blog'

router = DefaultRouter()
router.register('posts', PostsViewSet)
router.register('users', UsersViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
