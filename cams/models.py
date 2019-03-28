from django.db import models

# Create your models here.
class Address(models.Model):
    ip = models.GenericIPAddressField('IP', protocol='ipv4')
    port = models.IntegerField('Порт', default=554)

    def __str__(self):
        return self.ip

class House(models.Model):
    name = models.CharField('Дом', max_length=100)
    number = models.IntegerField('Номер')
    ip_address = models.ForeignKey(Address, on_delete='CASCADE')

    def __str__(self):
        return self.name

class Camera(models.Model):
    STANDART = 'G%s_P%sC%s'
    FRONT = 'G%s_F%s'
    CHOICES_MASK = (
        (STANDART, 'G(дом)_P(подъезд)C(номер)'),
        (FRONT, 'G(дом)_F(номер)'),
        )

    OUTSIDE = 'out'
    INSIDE = 'in'
    CHOICES_TYPE = (
        (OUTSIDE, 'Внешняя'),
        (INSIDE, 'Внутренняя'),
    )


    number = models.IntegerField('Номер')
    entrance = models.IntegerField('Подъезд')
    mask = models.CharField('Маска', choices=CHOICES_MASK, default=STANDART, max_length=100)
    cam_type = models.CharField('Тип', choices=CHOICES_TYPE, default=OUTSIDE, max_length=3)
    house = models.ForeignKey(House, on_delete='CASCADE')
    rtsp_link = models.CharField('RTSP ссылка', null=True, blank=True, max_length=100)

    def __str__(self):
        return '%s %sп, %s' % (self.house.name, self.entrance, self.number)
        
