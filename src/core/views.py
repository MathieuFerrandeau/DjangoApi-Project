from django.shortcuts import render
from django.http import JsonResponse


def test_view(request):
    data = {
        'name': 'jhon',
        'age': '33'
    }
    return JsonResponse(data)
