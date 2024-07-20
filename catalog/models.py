from django.db import models


class Product(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name="Наименование")
    description = models.TextField(
        verbose_name="Описание",
        blank=True,
        null=True,
    )
    image = models.ImageField(
        upload_to='catalog/image',
        verbose_name="Изображение",
        blank=True,
        null=True
    )
    category = models.ForeignKey(
        'Category',
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        blank=True,
        null=True,
        related_name="products",
    )
    price = models.IntegerField(
        verbose_name="Цена за покупку"
    )
    created_at = models.DateField(
        blank=True,
        null=True,
        verbose_name="Дата создания"
    )
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Дата последнего изменения"
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


class Category(models.Model):
    name = models.CharField(max_length=200, verbose_name="Наименование")
    description = models.TextField(verbose_name="Описание", blank=True, null=True)


def __str__(self):
    return f"{self.name} {self.description}"


class Meta:
    verbose_name = "Категория"
    verbose_name_plural = "Категории"
