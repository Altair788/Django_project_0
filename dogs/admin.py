from django.contrib import admin

from dogs.models import Dog, Breed, Parent


# Register your models here.
@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
        "breed",
    )
    list_filter = ("breed",)
    search_fields = ("name",)


@admin.register(Breed)
class BreedAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )


@admin.register(Parent)
class ParentAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "name",
    )
