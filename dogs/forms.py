from django.forms import ModelForm

from dogs.models import Dog, Parent


class DogForm(ModelForm):
    class Meta:
        model = Dog
        # fields = ('__all__')
        exclude = ("views_counter",)


class ParentForm(ModelForm):
    model = Parent
    fields = '__all__'

