from django.urls import path
from .views import RegisterCustomer,CustomerList,UsersDetail,OrderList,CreateOrder,CreateComment

app_name = "customer-app"
urlpatterns = [
    path('register/', RegisterCustomer.as_view(), name="customer-register"),
    path('customers/', CustomerList.as_view(), name="customer-list"),
    path('users/update/<int:pk>', UsersDetail.as_view(), name="customer-detail"),
    path('orders/', OrderList.as_view(), name="customer-orders"),
    path('orders/create', CreateOrder.as_view(), name="customer-create-order"),
    path('orders/comment', CreateComment.as_view(), name="customer-create-comment"),
    # path('restaurants/', RestaurantList.as_view(), name="r-list"),

    # path('orders/update', updateOrder.as_view(), name="r-update-order"),

]
