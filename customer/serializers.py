from  rest_framework import  serializers
from  .models import Customer
from restaurant.models import Comment
from restaurant.models import Order
from django.contrib.auth.models import  User

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username","password")

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )
        user.save()
        return user


class CustomerSerializers(serializers.ModelSerializer):
    User = serializers.CharField(source="User.username",read_only=True)
    class Meta:
        model = Customer
        fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
    User = serializers.CharField(source="User.username",read_only=True)
    Restaurant = serializers.CharField(source="Restaurant.name",read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'