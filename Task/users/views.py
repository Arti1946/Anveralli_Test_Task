from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CreationForm
from .models import CustomUser


class SignUp(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy("orders:orders_list")
    template_name = "users/signup.html"


def user_profile(request, user_id):
    profile = get_object_or_404(CustomUser, id=user_id)
    return render(request, "users/profile.html", {"profile": profile})
