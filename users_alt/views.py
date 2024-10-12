from django.urls import reverse_lazy
from django.views.generic import CreateView

from users_alt.forms import UserRegisterForm
from users_alt.models import User


class UserCreateView(CreateView):

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_alt:login")