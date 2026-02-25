from django.shortcuts import render
from .models import SliderItem


def slider_view(request):
    items = SliderItem.objects.all()
    return render(request, 'gallery/slider.html', {'items': items})
