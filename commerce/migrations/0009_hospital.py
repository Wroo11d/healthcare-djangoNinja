# Generated by Django 3.2.9 on 2022-01-09 18:33

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0008_auto_20220109_2124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='Hospitals/', verbose_name='image')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('open_time', models.TimeField(blank=True, null=True, verbose_name='open_time')),
                ('close_time', models.TimeField(blank=True, null=True, verbose_name='close_time')),
                ('days', models.TextField(blank=True, null=True, verbose_name='days')),
                ('location', models.TextField(blank=True, null=True, verbose_name='location')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
