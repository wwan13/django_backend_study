from.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        # fields = '__all__'
        fields = ['id', 'title', 'body']
        read_only_fields = ('title',)  # 읽기전용