from django.db import models

from users.models import User


# Create your models here.


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")
    description = models.TextField(max_length=300, verbose_name="Описание")
    photo = models.ImageField(upload_to="photo", blank=True, null=True)
    category = models.ForeignKey(
        "Category", on_delete=models.SET_NULL, null=True, blank=True
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        auto_now=True, verbose_name="Дата последнего изменения"
    )
    owner = models.ForeignKey(User, verbose_name='Владелец', help_text='Укажите владельца', blank=True, null=True, on_delete=models.SET_NULL)

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
        ordering = ("name", "category")

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименованик")
    description = models.TextField(verbose_name="Описание")

    class Meta:
        verbose_name = "категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.name


class Version(models.Model):
    name = models.ForeignKey(Product, verbose_name='Продукт', on_delete=models.CASCADE, related_name='versions')
    version_number = models.PositiveIntegerField(verbose_name='Номер версии')
    version_name = models.CharField(max_length=100, verbose_name="Название версии")
    version_now = models.BooleanField(
        default=True, verbose_name="Признак текущей версии"
    )

    class Meta:
        verbose_name = "Версия"
        verbose_name_plural = "Версии"

    def __str__(self):
        return f"{self.version_name} | {self.version_number}"
