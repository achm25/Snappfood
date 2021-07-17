from django.urls import path
from .views import RestaurantList, RestaurantDetail, RestaurantUpdateDetail, UsersList, UsersDetail, MenuList, \
    OrderList, AddFood, UpdateFood,RegisterRestaurnt,UpdateOrderStatus,RestaurantCommentList,SendReply,Search

app_name = "restaurant-app"
urlpatterns = [
    path('restaurants/', RestaurantList.as_view(), name="r-list"),
    path('<int:pk>', RestaurantDetail.as_view(), name="r-detail"),
    path('update/<int:pk>', RestaurantUpdateDetail.as_view(), name="r-detail"),
    path('users', UsersList.as_view(), name="r-detail"),
    path('users/update/<int:pk>', UsersDetail.as_view(), name="r-detail"),
    path('menu/', MenuList.as_view(), name="r-menu"),
    path('comments/', RestaurantCommentList.as_view(), name="c-order"),
    path('comments/reply/<int:pk>', SendReply.as_view(), name="c-order"),
    path('orders/', OrderList.as_view(), name="r-order"),
    path('orders/update/<int:pk>', UpdateOrderStatus.as_view(), name="r-order"),
    path('foods', AddFood.as_view(), name="r-order"),
    path('foods/update/<int:pk>', UpdateFood.as_view(), name="f-update"),
    path('register/', RegisterRestaurnt.as_view(), name="r-register"),
    path('search/', Search.as_view(), name="r-search"),
    # path('orders/update', updateOrder.as_view(), name="r-update-order"),

]
