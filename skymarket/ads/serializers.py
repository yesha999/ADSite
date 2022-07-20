from ads.models import Ad, Comment
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    pk = serializers.IntegerField(source="author.id", read_only=True)

    class Meta:
        model = Comment
        fields = '__all__'


class AdSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    pk = serializers.IntegerField(source="author.id", read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'


class AdListMeSerializer(serializers.ModelSerializer):
    author_first_name = serializers.CharField(source="author.first_name", read_only=True)
    author_last_name = serializers.CharField(source="author.last_name", read_only=True)
    author_id = serializers.IntegerField(source="author.id", read_only=True)
    pk = serializers.IntegerField(source="author.id", read_only=True)

    class Meta:
        model = Ad
        fields = '__all__'
