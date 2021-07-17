from .models import Customer
from  restaurant.models import Restaurant,Comment
from .serializers import CustomerSerializers, UserSerializers,CommentSerializer

from django.http import HttpResponse, JsonResponse
from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, \
    CreateAPIView, RetrieveUpdateAPIView
from rest_framework.views import APIView
from django.contrib.auth.models import User
from rest_framework.permissions import IsAdminUser
from rest_framework.response import Response
from rest_framework import status
from restaurant.models import  Order
from restaurant.serializers import  OrderSerializer

# Create your views here.
class RegisterUser(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


class RegisterCustomer(APIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    def post(self, request, *args, **kwargs):
        user = User.objects.get(username=request.data['User'])
        request.data['User'] = user
        serializer = CustomerSerializers(data=request.data,)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)


class CustomerList(ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializers
    filterset_fields = ["User__username"]


class UsersDetail(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializers


#get restaurant order by id
class OrderList(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ['User__username', ]


#customer buy food
class CreateOrder(APIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    def post(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.get(name=request.data['Restaurant'])
        user = User.objects.get(username=request.data['User'])
        request.data['User'] = user
        request.data['Restaurant'] = restaurant
        serializer = OrderSerializer(data=request.data,)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)



#customer buy food
class CreateComment(APIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    def post(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.get(name=request.data['Restaurant'])
        user = User.objects.get(username=request.data['User'])
        request.data['User'] = user
        request.data['Restaurant'] = restaurant
        serializer = CommentSerializer(data=request.data,)
        if serializer.is_valid(raise_exception=ValueError):
            serializer.create(validated_data=request.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.error_messages,
                        status=status.HTTP_400_BAD_REQUEST)