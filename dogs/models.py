from django.db import models

import dogs.models

NULLABLE = {"blank": True, "null": True}


# Create your models here.


class Dog(models.Model):
    """
    Представляет класс Собака
    """

    name = models.CharField(
        max_length=100, verbose_name="Кличка", help_text="Введите кличку собаки"
    )
    breed = models.ForeignKey(
        to='Breed',
        on_delete=models.SET_NULL,
        **NULLABLE,
        verbose_name="Порода",
        help_text="Введите породу собаки",
        #  у породы будет неявный параметр собаки, т к у одной породы
        #  может быть много собак
        related_name='dogs',
    )
    photo = models.ImageField(
        upload_to="dogs/photo",
        **NULLABLE,
        verbose_name="Фото",
        help_text="Загрузите фото собаки",
    )
    date_born = models.DateField(
        **NULLABLE, verbose_name="Дата рождения", help_text="Укажите дату рождения"
    )
    views_counter = models.PositiveIntegerField(
        verbose_name="Счетчик просмотров",
        help_text="Укажите количество просмотров",
        default=0
    )

    def __str__(self):
        """
        Строковое представление класса Собака
        """
        return (
            f"{self.name}, {self.date_born} г.р., порода: {self.breed}"
        )

    class Meta:
        verbose_name = "собака"
        verbose_name_plural = "собаки"
        ordering = (
            "date_born",
            "breed",
            "name",
        )


class Breed(models.Model):
    """
    Представляет класс Порода
    """

    name = models.CharField(
        max_length=100,
        verbose_name="Название породы",
        help_text="Введите название породы",
    )
    description = models.TextField(
        verbose_name="Описание породы", help_text="Введите описание породы", **NULLABLE
    )

    def __str__(self):
        """
        Строковое представление класса Порода
        """
        return f"{self.name}"

    class Meta:
        verbose_name = "порода"
        verbose_name_plural = "породы"
