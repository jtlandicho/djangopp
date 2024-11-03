from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import RegisterForm

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log the user in after registration (optional)
            return redirect('dashboard')  # Redirect to a desired page after registration
    else:
        form = RegisterForm()

    return render(request, 'accounts/register.html', {'form': form})