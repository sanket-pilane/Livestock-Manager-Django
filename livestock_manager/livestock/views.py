
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy
from .models import Livestock
from .forms import CustomUserCreationForm, LivestockForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'livestock/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'livestock/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def dashboard(request):
    livestock = Livestock.objects.filter(owner=request.user)
    return render(request, 'livestock/dashboard.html', {'livestock': livestock})

class LivestockCreateView(LoginRequiredMixin, CreateView):
    model = Livestock
    form_class = LivestockForm
    template_name = 'livestock/livestock_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class LivestockUpdateView(LoginRequiredMixin, UpdateView):
    model = Livestock
    form_class = LivestockForm
    template_name = 'livestock/livestock_form.html'
    success_url = reverse_lazy('dashboard')

class LivestockDeleteView(LoginRequiredMixin, DeleteView):
    model = Livestock
    template_name = 'livestock/livestock_confirm_delete.html'
    success_url = reverse_lazy('dashboard')
