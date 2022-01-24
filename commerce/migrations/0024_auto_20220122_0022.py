# Generated by Django 3.2.9 on 2022-01-21 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0023_auto_20220122_0005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='HospitalType',
        ),
        migrations.AddField(
            model_name='hospitaltype',
            name='HospitalCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='HospitalType', to='commerce.hospitalcategory'),
        ),
    ]
