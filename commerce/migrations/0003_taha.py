# Generated by Django 3.2.9 on 2021-11-05 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0002_layth_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Taha',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]
