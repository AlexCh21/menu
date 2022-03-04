from django.shortcuts import render
from .models import DATA


def recipes_list(request):
    calculator = ''
    for i in range(len(DATA)):
        calculator += f"<a href='{i}/'>{DATA[i]['name']}</a><br>"
    context = {
        'calculator': calculator,
    }
    return render(request, 'recepe/recipes-list.html', context)


def recipes_detail(request, pk):
    name = DATA[pk]['name']
    description = DATA[pk]['description']
    context = {
        'name': name,
        'description': description,
    }
    return render(request, 'recepe/recipes-detail.html', context)
