from ads.views import AdListMeView
from ads.views import AdViewSet, CommentViewSet
from django.urls import include, path
from rest_framework import routers

ad_list = AdViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
ad_detail = AdViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

router = routers.SimpleRouter()
router.register('comments', CommentViewSet, basename="")

urlpatterns = [
    path("ads/", ad_list),
    path("ads/<int:pk>/", ad_detail),
    path("ads/<int:ad_id>/", include(router.urls)),
    path("ads/me/", AdListMeView.as_view())
]
