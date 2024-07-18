from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наименование категории")
    description = models.TextField(
        verbose_name="Описание категории", blank=True, null=True
    )


def __str__(self):
    return f"{self.name} {self.description}"


class Meta:
    verbose_name = "категория"
    verbose_name_plural = "категории"


class Product(models.Model):
    name = models.CharField(
        max_length=100,
        verbose_name="Наименование"
    )
    description = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Описание",
        blank=True,
        null=True,
        related_name="products"
    )
    image = models.ImageField(
        verbose_name="Изображение", blank=True, null=True
    )
    category = models.CharField(max_length=150, verbose_name="Категория")
    price = models.IntegerField(verbose_name="Цена за покупку")
    created_at = models.DateField(blank=True, null=True, verbose_name="Дата создания")
    updated_at = models.DateField(
        blank=True, null=True, verbose_name="Дата последнего изменения"
    )
    manufactured_at = models.DateField(blank=True, null=True, verbose_name="Дата производства продукта")

    def __str__(self):
        return (
            f"{self.name}/n"
            f" {self.description}/n"
            f" {self.image}/n"
            f" {self.category}/n"
            f"{self.price}/n"
            f" {self.created_at}/n"
            f"{self.updated_at}"
        )

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"
