from django.shortcuts import render
from .models import Asset

def asset_list(request):
    context = {
        "assets" : Asset.objects.all()
    }
    return render(request, 'assets/asset_list.html', context)