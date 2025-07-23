from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Built-in Django form for user creation
from django.urls import reverse_lazy # To redirect after successful registration

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(reverse_lazy('login')) # Redirect to login page after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

# Create your views here.
