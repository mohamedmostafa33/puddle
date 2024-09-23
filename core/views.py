from django.shortcuts import render, redirect
from django.contrib.auth.views import LogoutView as BaseLogoutView
from django.urls import reverse_lazy
from item.models import Category, Item
from .forms import SignupForm

def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories': categories,
        'items': items,
    })

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('core:login')   
    else:
        form = SignupForm()
    return render(request, 'core/signup.html', {'form': form})

class LogoutView(BaseLogoutView):
    next_page = reverse_lazy('core:login')   
