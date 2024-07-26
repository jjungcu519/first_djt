from django.shortcuts import render
import random

# Create your views here.
def index(request): #self와 비슷
    return render(request, 'index.html')

def root(request):
    return render(request, 'root.html')

def hello(request):
    username = 'JA_519' #데이터베이스에서 가져올거임~

    context = {
        'name' : username,
    }

    return render(request, 'hello.html', context)

def lunch(request):
    menus = ['🍣 스시', '🍜라면', '🍝 파스타', '🍔 햄버거', '🌭 핫도그', '🌮 타코']
    pick_today = random.choice(menus)

    context = {
        'pick' : pick_today
    }
    return render(request, 'lunch.html', context)

def lotto(request):
    pick_lotto = random.sample(range(1, 46), 6)

    context = {
        'lotto' : pick_lotto
    }
    
    return render(request, 'lotto.html', context)


