# Generated by Django 5.0.6 on 2024-06-12 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0004_delete_blog"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="viewed",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Укажите количество просмотров",
                verbose_name="Счетчик просмотров",
            ),
        ),
    ]
