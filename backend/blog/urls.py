from rest_framework.routers import DefaultRouter
from .views import BlogPostViewSet, TagViewSet, CategoryViewSet, AuthorViewSet

router = DefaultRouter()
router.register('posts', BlogPostViewSet)
router.register('tags', TagViewSet)
router.register('categories', CategoryViewSet)
router.register('authors', AuthorViewSet)

urlpatterns = router.urls
