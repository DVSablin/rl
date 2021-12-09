from django.db import models

# Create your models here.


class Order(models.Model):
    ORDER_STATUS = [
        ('RECIEVED', 'Получен'),
        ('TAKEN', 'Принят'),
        ('FINISHED', ' Выполнен'),
        ('REJECTED', 'Отменен')
    ]
    name = models.CharField(max_length=100, verbose_name='Имя')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.CharField(max_length=100, verbose_name='Email')
    departure = models.CharField(max_length=100, verbose_name='Откуда')
    arrival = models.CharField(max_length=100, verbose_name='Куда')
    weight = models.DecimalField( max_digits=10, decimal_places=2 ,verbose_name='Вес')
    capacity = models.DecimalField(max_digits=10, decimal_places=2 , verbose_name='Объем')
    length = models.DecimalField( max_digits=10, decimal_places=2 ,verbose_name='Длина', null=True, blank=True)
    height = models.DecimalField(max_digits=10, decimal_places=2 ,verbose_name='Высота', null=True, blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2 ,verbose_name='Ширина', null=True, blank=True)
    date = models.DateField(verbose_name='Дата отправки', blank=True, null=True)
    arrival_date = models.DateField(verbose_name='Дата выгрузки', blank=True, null=True)
    extra_info = models.TextField(max_length=255, blank=True, null=True, verbose_name='Комментарии к заявке')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата получения')
    order_status = models.CharField(max_length=10, choices=ORDER_STATUS, verbose_name='Статус заказа', null=True, blank='True', default='RECIEVED' )

    def __str__(self):
        return f'{self.name} - {self.phone}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    secondary_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    birthday = models.DateField()
    experience = models.PositiveIntegerField()



class DriverLicence(models.Model):
    employee_id = models.OneToOneField(Employee, on_delete=models.CASCADE)
    receive_date = models.DateField()
    expire_date = models.DateField()






    