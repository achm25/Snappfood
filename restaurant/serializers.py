from  rest_framework import  serializers
from  .models import Restaurant,Food,Order,Comment
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


class RestaurantSerializers(serializers.ModelSerializer):
    manager = serializers.CharField(source="manager.username",read_only=True)
    class Meta:
        model = Restaurant
        fields = '__all__'

    def menu(self, obj):
        return Food.objects.filter(Restaurant=obj)



class FoodSerializer(serializers.ModelSerializer):
    Restaurant = serializers.CharField(source="Restaurant.name",read_only=True)
    class Meta:
        model = Food
        fields = '__all__'



class FoodSearchSerializer(serializers.ModelSerializer):
    Restaurant = serializers.CharField(source="Restaurant.name",read_only=True)
    Restaurant_district = serializers.CharField(source="Restaurant.district",read_only=True)
    Restaurant_status = serializers.CharField(source="Restaurant.status",read_only=True)
    Restaurant_price = serializers.CharField(source="Restaurant.price",read_only=True)
    Restaurant_name = serializers.CharField(source="Restaurant.name",read_only=True)
    Restaurant_from = serializers.CharField(source="Restaurant.fromTime",read_only=True)
    Restaurant_to = serializers.CharField(source="Restaurant.toTime",read_only=True)
    Restaurant_id = serializers.CharField(source="Restaurant.id",read_only=True)
    class Meta:
        model = Food
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    User = serializers.CharField(source="User.username",read_only=True)
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('RestaurantComment',)

class OrderSerializer(serializers.ModelSerializer):
    User = serializers.CharField(source="User.username",read_only=True)
    Restaurant = serializers.CharField(source="Restaurant.name",read_only=True)
    class Meta:
        model = Order
        fields = '__all__'


class UpdateOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ('state',)



class RestaurantUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ('name','district','address','fromTime','toTime','price','status','id')

    def menu(self, obj):
        return Food.objects.filter(Restaurant=obj)



