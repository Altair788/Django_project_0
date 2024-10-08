from django.forms import ModelForm

from dogs.models import Dog


class DogForm(ModelForm):
    class Meta:
        model = Dog
        # fields = ('__all__')
        exclude = ("views_counter",)
