from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Restaurant(models.Model):
    name = models.CharField(max_length=200,)
    idName = models.SlugField(max_length=100, unique=True)
    manager = models.ForeignKey(User, on_delete=models.CASCADE)
    district = models.CharField(max_length=50)
    address = models.CharField(max_length=200)
    fromTime = models.CharField(max_length=10)
    toTime = models.CharField(max_length=10)
    price = models.CharField(max_length=200)
    status = models.CharField(max_length=2)

    # Create your models here.
    def __str__(self):
        return self.name





class Food(models.Model):
    Name = models.CharField(max_length=100)
    Status = models.BooleanField(default=True)
    Price = models.IntegerField(null=False)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)

    # def __init__(self, Name, Status, Price,Restaurant,score):
    #     self.Name = Name
    #     self.Status = Status
    #     self.Price = Price
    #     self.Restaurant = Restaurant
    #     self.score = score


    # Create your models here.
    def __str__(self):
        return self.Name


class Order(models.Model):
    class OrderState(models.TextChoices):
        AWAITING_APPROVAL = 'AWAITING_APPROVAL'
        PREPARING = 'PREPARING'
        SENDING = 'SENDING'
        DELIVERED = 'DELIVERED'

    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Food = models.ManyToManyField(Food)
    OrderCost = models.IntegerField(null=False)
    ApproximateArrivalTime = models.DateTimeField()
    state = models.CharField(choices=OrderState.choices, max_length=100)

    def add_food_to_order(self, Foods):
        for food in Foods:
            self.Food.add(food)
            self.OrderCost += food.Price


#todo add order foreign key
class Comment(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    Restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    Time = models.DateTimeField(default=datetime.now, blank=True)
    UserComment = models.CharField(max_length=160)
    RestaurantComment = models.CharField(max_length=160,blank=True, null=True)
    score = models.IntegerField(default=0)