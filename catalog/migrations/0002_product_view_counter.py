# Generated by Django 5.0.6 on 2024-05-26 23:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="view_counter",
            field=models.PositiveIntegerField(
                default=0,
                help_text="Укажите кол-во просмоторов",
                verbose_name="Счетчик просомтров",
            ),
        ),
    ]
