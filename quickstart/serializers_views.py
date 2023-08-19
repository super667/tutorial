from datetime import datetime

class Comment:
    def __init__(self, email, content, created=None) -> None:
        self.email = email
        self.content = content 
        self.created = created or datetime.now()


comment = Comment(email='leila@example.com', content='foo bar')


from rest_framework import serializers

class CommentSerializer(serializers.Serializer):
    email = serializers.EmailField()
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()

    def create(self, validated_data):
        return Comment(**validated_data)

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.content = validated_data.get('content', instance.content)
        instance.created = validated_data.get('created', instance.created)
        return instance



serializer = CommentSerializer(comment)
serializer.data


import io
from rest_framework.parsers import JSONParser
stream = io.BytesIO(json)
data = JSONParser().parse(stream)


class BolgPostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    content = serializers.CharField()

    def validate_title(self, value):
        """
        check that the blog post is about Django.
        """
        if 'django' not in value.lower():
            raise serializers.ValidationError("Blog post is not about Django")
        return value




class EventSerializer(serializers.Serializer):
    description = serializers.CharField(max_length=100)
    start = serializers.DateTimeField()
    finish = serializers.DateTimeField()


    def validate(self, data):
        """
        check that start is before finish.
        """
        if data['start'] > data['finish']:
            raise serializers.ValidationError("finish must occur after start")
        
        return data



def multiple_of_ten(value):
    if value % 10 != 0:
        raise serializers.ValidationError("Not a nultiple of ten")

class GameRecord(serializers.Serializer):
    score = serializers.IntegerField(validators=[multiple_of_ten])


class UserSerializer(serializers.Serializer):
    email = serializers.EmailField()
    username = serializers.CharField()

class CommentSerializer(serializers.Serializer):
    user = UserSerializer(required=False)
    content = serializers.CharField(max_length=200)
    created = serializers.DateTimeField()



class UserSerializer2(serializers.Serializer):