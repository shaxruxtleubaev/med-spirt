from django.db.models import *
from image_optimizer.fields import OptimizedImageField
from django.utils.timezone import *

class Client(Model):

    fullname = CharField(
        'ФИО',
        max_length=256,
    )

    phone_number = CharField(
        'Номер телефона',
        max_length=256
    )

    date = DateField(
        verbose_name='Дата заказа',
        default=now,
        blank=True,
        null=True
    )

    def __str__(self):
        return f'{self.fullname}'

    class Meta:

        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

class Blog(Model):

    image = OptimizedImageField(
        upload_to='blog-images/%Y/%m/%d',
        optimized_image_output_size=(640, 480),
        optimized_image_resize_method='cover'
    )

    title = CharField(
        'Название блога',
        max_length=256
    )

    text = TextField(
        'Текст'
    )

    date = DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.title}'
    
    class Meta:

        verbose_name = 'пост'
        verbose_name_plural = 'посты'

class Sponsor(Model):

    name = CharField(
        'Имя спонсора',
        max_length=128
    )

    image = OptimizedImageField(
        upload_to = 'sponsor-images/%Y/%m/%d',
        optimized_image_output_size=(640, 480),
        optimized_image_resize_method='cover' 
    )

    def __str__(self):
        return f'{self.name}'

    class Meta:

        verbose_name = 'спонсор'
        verbose_name_plural = 'спонсоры'

class Product(Model):

    name = CharField(
        'Имя продукта',
        max_length=128
    )

    description = TextField(
        'Описание продукта'
    )

    image = OptimizedImageField(
        upload_to='product-images/%Y/%m/%d',
        optimized_image_output_size=(640, 480),
        optimized_image_resize_method='cover'
    )

    def __str__(self):
        return f'{self.name}'
    
    class Meta:

        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
