# Generated by Django 4.2.2 on 2024-10-15 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dogs", "0006_dog_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="dog",
            options={
                "ordering": ("date_born", "breed", "name"),
                "permissions": [
                    ("can_edit_breed", "can edit breed"),
                    ("can_edit_description", "can edit description"),
                ],
                "verbose_name": "собака",
                "verbose_name_plural": "собаки",
            },
        ),
        migrations.AddField(
            model_name="dog",
            name="description",
            field=models.TextField(
                blank=True,
                help_text="Введите описание собаки",
                null=True,
                verbose_name="Описание собаки",
            ),
        ),
    ]