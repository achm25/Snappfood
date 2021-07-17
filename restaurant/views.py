from .models import Restaurant, Food, Order,Comment
from .serializers import RestaurantSerializers, UserSerializers, FoodSerializer, OrderSerializer, \
    RestaurantUpdateSerializers,UpdateOrderSerializer,CommentSerializer,ReplySerializer,FoodSearchSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, \
    CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status





class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers

class RegisterRestaurnt(APIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializers
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['manager'])
        request.data['manager'] = user
        serializer = RestaurantSerializers(data=request.data,)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)



#......
class AddFood(APIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

    def post(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.get(name=request.data['Restaurant'])
        request.data['Restaurant'] = restaurant
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        snippet = Food.objects.get(pk=request.data['id'])
        snippet.delete()
        return Response(status=status.HTTP_200_OK)


class MenuList(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    filterset_fields = ['Restaurant__id', ]
    ordering_fields = ['score']
    ordering = ['-score']


# change specif food detail
class UpdateFood(RetrieveUpdateDestroyAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer

#get restaurant order by id
class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ['Restaurant__id', ]

class UpdateOrderStatus(RetrieveUpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = UpdateOrderSerializer

class RestaurantCommentList(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filterset_fields = ['Restaurant__id', ]

class SendReply(RetrieveUpdateAPIView):
    queryset = Comment.objects.all()
    serializer_class = ReplySerializer

class Search(ListAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSearchSerializer
    filterset_fields = ['Name','Restaurant__name', ]
    ordering = ['-Status']
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Restaurant.objects.all()
    #     district = self.request.query_params.get('Restaurant_district')
    #     print("Ssssss")
    #     print(district)
    #     status = self.request.query_params.get('status')
    #     if district is not None:
    #         queryset = queryset.filter(Restaurant_district=district)
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #
    #     return queryset

    # ordering_fields = ['Price']
    # ordering = ['-price']


class RestaurantList(ListCreateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializers
    filterset_fields = ['district', 'status', "manager__username"]
    ordering_fields = ['price']
    ordering = ['-price']
    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     queryset = Restaurant.objects.all()
    #     district = self.request.query_params.get('district')
    #     status = self.request.query_params.get('status')
    #     if district is not None:
    #         queryset = queryset.filter(district=district)
    #     if status is not None:
    #         queryset = queryset.filter(status=status)
    #
    #     return queryset

    # def get_queryset(self):
    #     user = self.request.user
    #     return Restaurant.objects.filter(manager=user,status="o")


class RestaurantDetail(RetrieveAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializers


class RestaurantUpdateDetail(RetrieveUpdateAPIView):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantUpdateSerializers


class UsersList(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers
    permission_classes = (IsAdminUser,)


class UsersDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers





def home(request):
    context = {
        "retaurants": Restaurant.objects.all()
    }
    return HttpResponse(context)
