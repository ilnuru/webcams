# Generated by Django 2.1.7 on 2019-03-28 05:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cams', '0002_house_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='camera',
            name='rtsp_link',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='RTSP ссылка'),
        ),
    ]