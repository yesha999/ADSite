from ads.models import Ad, Comment
from ads.models import AdFilter
from ads.permissions import AdUpdatePermission, AdDeletePermission
from ads.serializers import AdListMeSerializer
from ads.serializers import AdSerializer, CommentSerializer
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import pagination, viewsets
from rest_framework.generics import ListAPIView
from rest_framework.permissions import IsAuthenticated


class AdPagination(pagination.PageNumberPagination):
    pass


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    serializer_class = AdSerializer
    filter_backends = (DjangoFilterBackend,)  # Подключаем библотеку, отвечающую за фильтрацию к CBV
    filterset_class = AdFilter  # Выбираем наш фильтр

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(author=user)

    def get_permissions(self):
        if self.action == 'list' or 'retrieve':
            permission_classes = []
        else:
            permission_classes = [IsAuthenticated]
            if self.action == 'destroy':
                permission_classes.append(AdDeletePermission)
            if self.action == 'update' or "partial_update":
                permission_classes.append(AdUpdatePermission)
        return [permission() for permission in permission_classes]


class AdListMeView(ListAPIView):
    serializer_class = AdListMeSerializer

    def get_queryset(self):
        user = self.request.user
        new_queryset = Ad.objects.filter(author=user.pk)
        return new_queryset


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer

    def get_queryset(self):
        ad_id = self.kwargs.get("ad_id")
        new_queryset = Comment.objects.filter(ad=ad_id)
        return new_queryset

    def perform_create(self, serializer):
        user = self.request.user
        ad_id = self.kwargs.get("ad_id")
        ad = get_object_or_404(Ad, pk=ad_id)
        serializer.save(author=user, ad=ad)

    def get_permissions(self):
        permission_classes = [IsAuthenticated]
        if self.action == 'destroy':
            permission_classes.append(AdDeletePermission)
        if self.action == 'update' or "partial_update":
            permission_classes.append(AdUpdatePermission)

        return [permission() for permission in permission_classes]
