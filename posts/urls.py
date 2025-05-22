from django.urls import path
from  rest_framework.routers import DefaultRouter
from posts.views import LikeView, PostViewSet, CommentViewSet

router = DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns =  [
        path('like/<int:post_id>/', LikeView.as_view())
] +router.urls