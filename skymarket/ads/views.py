from ads.models import Ad, Comment
from ads.serializers import AdListMeSerializer
from ads.serializers import AdSerializer, CommentSerializer
from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView


class AdPagination(pagination.PageNumberPagination):
    pass


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer


class AdListMeView(ListAPIView):
    serializer_class = AdListMeSerializer

    def get_queryset(self):
        user = self.request.user
        print("ниже будет юзер пк")
        print(user.pk)
        new_queryset = Ad.objects.filter(author=user.pk)
        return new_queryset

    # permission_classes = [IsAuthenticated]


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_id")
        new_queryset = Comment.objects.filter(ad=ad_id)
        return new_queryset
