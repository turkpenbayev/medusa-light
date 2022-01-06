from rest_framework_nested import routers

from news.views import NewsViewSet

router = routers.SimpleRouter()
router.register('news', NewsViewSet, basename='constants')

urlpatterns = [
    *router.urls,
]