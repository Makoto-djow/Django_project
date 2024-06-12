from django.db import models

# Create your models here.


class Blog(models.Model):
    name = models.CharField(max_length=100, verbose_name="Заголовок")
    slug = models.SlugField(blank=True, null=True, max_length=150, unique=True, verbose_name="slug")
    description = models.TextField(blank=True, null=True, verbose_name="Описание")
    photo = models.ImageField(blank=True, null=True, upload_to='blog/photo', verbose_name='Изображение', help_text='Выберите изображение')
    created_at = models.DateField(blank=True, null=True, verbose_name="Дата создание записи", auto_now_add=True, editable=False)
    updated_at = models.DateField(blank=True, null=True, verbose_name="Дата последнего изменения")
    viewed = models.PositiveIntegerField(verbose_name='Счетчик просмотров', help_text="Укажите количество просмотров", default=0)

    class Meta:
        verbose_name = "Блог"
        verbose_name_plural = "Блоги"
        ordering = ["name", "created_at", "updated_at"]

    def __str__(self):
        return self.name
