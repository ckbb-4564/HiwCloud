from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_foods, name='foods'),
    path('<int:food_id>', views.get_food, name='food')
]