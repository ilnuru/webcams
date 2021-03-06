# Generated by Django 2.1.7 on 2019-03-28 11:15

from django.db import migrations


def forwards_func(apps, schema_editor):
    from django.contrib.auth import get_user_model

    user_model = get_user_model()
    obj = user_model(
        username='admin',
        is_superuser=True,
        is_staff=True,
        is_active=True
    )
    obj.set_password('1q1q1q')
    obj.save()


class Migration(migrations.Migration):
    dependencies = [
        ('cams', '0004_auto_20190328_0914'),
    ]

    operations = [
        migrations.RunPython(forwards_func, lambda x: x)
    ]