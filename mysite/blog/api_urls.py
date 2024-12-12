# blog/api_urls.py
from rest_framework.routers import DefaultRouter
from .views import BlogViewSet, CommentViewSet, LikeBlogViewSet

router = DefaultRouter()
router.register(r'blogs', BlogViewSet, basename='blog')
router.register(r'blogcomments', CommentViewSet, basename='blog-comment')
router.register(r'likeblogs', LikeBlogViewSet, basename='like-blog')

urlpatterns = router.urls
