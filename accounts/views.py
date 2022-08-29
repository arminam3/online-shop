from django.shortcuts import render
from django.views.generic import CreateView
from django.contrib.auth import get_user_model
from django.urls import reverse_lazy

from .forms import CustomUserCreatoionForm


class RegisterView(CreateView):
    model = get_user_model()
    template_name = "account/register.html"
    form_class = CustomUserCreatoionForm
    success_url = reverse_lazy('account:home')

