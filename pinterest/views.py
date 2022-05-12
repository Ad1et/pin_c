from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from posts.models import Pin


@login_required
def home(request):
    pins = Pin.objects.all()
    context = {'pins':pins[:49]}
    return render(request, 'main.html', context)


@login_required
def search(request):
    query = request.GET.get('q')
    pins = Pin.objects.filter(
        title__icontains=query,
        description__icontains=query).all()
    context = {'pins':pins[:49]}
    return render(request, 'main.html', context)