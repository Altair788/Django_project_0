# Generated by Django 5.1 on 2024-10-08 15:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0002_dog_views_counter"),
    ]

    operations = [
        migrations.CreateModel(
            name="Parent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="Введите кличку собаки",
                        max_length=100,
                        verbose_name="Кличка",
                    ),
                ),
                (
                    "year_born",
                    models.PositiveIntegerField(
                        blank=True,
                        default=0,
                        help_text="Укажите год рождения",
                        null=True,
                        verbose_name="Год рождения",
                    ),
                ),
                (
                    "breed",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите породу собаки",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="parent_dogs",
                        to="dogs.breed",
                        verbose_name="Порода",
                    ),
                ),
                (
                    "dog",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="parents",
                        to="dogs.dog",
                        verbose_name="Собака",
                    ),
                ),
            ],
            options={
                "verbose_name": "Собака - родитель",
                "verbose_name_plural": "Собаки - родители",
                "ordering": ("year_born", "breed", "name"),
            },
        ),
    ]
