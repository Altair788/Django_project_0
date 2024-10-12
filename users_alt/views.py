import secrets

from django.urls import reverse_lazy
from django.views.generic import CreateView

from users_alt.forms import UserRegisterForm
from users_alt.models import User


class UserCreateView(CreateView):

    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy("users_alt:login")


    def form_valid(self, form):
        #  сохраняем пользователя
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        self.request.get_host()
        url =
