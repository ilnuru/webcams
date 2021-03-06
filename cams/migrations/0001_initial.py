# Generated by Django 2.1.7 on 2019-03-28 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.GenericIPAddressField(protocol='ipv4', verbose_name='IP')),
                ('port', models.IntegerField(default=554, verbose_name='Порт')),
            ],
        ),
        migrations.CreateModel(
            name='Camera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(verbose_name='Номер')),
                ('entrance', models.IntegerField(verbose_name='Подъезд')),
                ('mask', models.CharField(choices=[('G(%s)_P(%s)C(%s)', 'G(дом)_P(подъезд)C(номер)')], default='G(%s)_P(%s)C(%s)', max_length=100, verbose_name='Маска')),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Дом')),
                ('ip_address', models.ForeignKey(on_delete='CASCADE', to='cams.Address')),
            ],
        ),
        migrations.AddField(
            model_name='camera',
            name='house',
            field=models.ForeignKey(on_delete='CASCADE', to='cams.House'),
        ),
    ]
