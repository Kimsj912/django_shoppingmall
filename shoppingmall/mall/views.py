from django.shortcuts import render, get_object_or_404
from .models import Mall

# Create your views here.
def home(request):
    malls = Mall.objects.all()
    return render(request, 'home.html', {'malls':malls})

def detail(request, mall_id):
    mall=get_object_or_404(Mall, pk=mall_id)
    return render(request, 'detail.html', {'mall':mall})