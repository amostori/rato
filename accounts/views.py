from django.shortcuts import render, redirect
from django.contrib import auth, messages
from .forms import CustomRegisterForm

def register(request):
    if request.method == 'POST':
        form = CustomRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, f'Account created successfully!')
            return redirect('home')
    else:
        form = CustomRegisterForm()
    return render(request, 'register.html', {'form': form})


# Create your views here.
