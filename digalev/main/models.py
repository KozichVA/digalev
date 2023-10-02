from django.db import models
from django.utils.timezone import now


class Category(models.Model):
    name = models.CharField(max_length=24, unique=True, blank=False, null=False)
    description = models.CharField(max_length=512)
    picture = models.ImageField(upload_to='category/', max_length=255)
    slug = models.SlugField(max_length=24, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категорию'
        verbose_name_plural = 'категории'


class Service(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE,
                                 db_index=True, verbose_name='категория')
    name = models.CharField(max_length=24, unique=True, blank=False,
                            null=False, verbose_name='название')
    description = models.CharField(max_length=512)
    picture = models.ImageField(upload_to='service/', max_length=255)
    slug = models.SlugField(max_length=24)
    is_published = models.BooleanField(default=False, verbose_name='опубликовать на главной')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'услуга'
        verbose_name_plural = 'услуги'


class Equipment(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE,
                                 db_index=True,  verbose_name='категория')
    name = models.CharField(max_length=24, unique=True, blank=False,
                            null=False, verbose_name='имя')
    description = models.CharField(max_length=512, verbose_name='описание')
    model = models.CharField(max_length=24, blank=True, null=True, verbose_name='модель станка',)
    picture = models.ImageField(upload_to='equipment/', max_length=255, verbose_name='фото')
    slug = models.SlugField(max_length=24)
    is_published = models.BooleanField(default=False, verbose_name='опубликовать на главной')


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'оборудование'
        verbose_name_plural = 'оборудование'


class CompletedWorks(models.Model):
    category = models.ForeignKey(to='Category', on_delete=models.CASCADE,
                                 db_index=True, verbose_name='категория')
    name = models.CharField(max_length=24, unique=True, blank=False,
                            null=False, verbose_name='название')
    description = models.CharField(max_length=512, verbose_name='описание')
    picture = models.ImageField(upload_to='completed_works/', max_length=255, verbose_name='картинка')
    slug = models.SlugField(max_length=24)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'выполненная работа'
        verbose_name_plural = 'выполненные работы'


class User(models.Model):
    name = models.CharField(max_length=24, unique=True, blank=False, null=False)
    telephone = models.CharField(max_length=24, unique=False, blank=False,
                                 null=False, verbose_name='телефон')
    mail = models.EmailField()
    description = models.CharField(max_length=24,  blank=True, null=True)
    is_mudak = models.BooleanField(default=False, verbose_name='мудак',
                                   blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'


class Order(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE,
                             db_index=True, verbose_name='клиент')
    description = models.CharField(max_length=512, verbose_name='описание')
    plan_file = models.FileField(upload_to='order/',  blank=True,
                                 null=True, verbose_name='чертеж')
    price = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True,)
    production_time = models.DateField(blank=True, null=True,)
    date_created = models.DateField(default=now, verbose_name='дата заявки')
    count = models.IntegerField(blank=True, null=True,)

    def __str__(self):
        return self.user.name

    @property
    def date(self):
        return self.date_created.strftime('%d %m %Y')

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'


