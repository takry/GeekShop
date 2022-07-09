from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=128, verbose_name='Название', unique=True)
    description = models.TextField(verbose_name='Описание', blank=True)

    def __str__(self):
        return f'#{self.pk}. {self.name}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ('name',)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='категория')
    name = models.CharField(verbose_name='Название', max_length=128)
    image = models.ImageField(upload_to='product', blank=True, null=True, verbose_name='Изображение')
    short_desc = models.CharField(verbose_name='краткое описание ', max_length=128)
    description = models.TextField(verbose_name='описание продукта')
    price = models.DecimalField(verbose_name='цена', max_digits=8, decimal_places=2, default=0)
    quantity = models.PositiveIntegerField(verbose_name='количество', default=0)

    def __str__(self):
        return f"{self.name} ({self.category.name})"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
