from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_user, name='login/'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('place_order/<int:product_id>/', views.place_order, name='place_order'),
    path('products/', views.products, name='products'),
    path('index/', views.index, name='index'),
    path("your_orders/", views.your_orders, name='your_orders'),
    path("user/", views.user, name='user'),
    path('delete_order/<int:id>/',views.delete_order,name="delete_order"),
]
