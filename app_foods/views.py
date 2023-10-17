from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def get_foods(request):
    return render(request, 'app_foods/foods.html')

def get_food(request, food_id):
    return render(request, 'app_foods/food.html', context={'food_id': food_id})