# Generated by Django 3.2.9 on 2022-01-24 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0033_auto_20220124_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='privatehospital',
            name='HospitalCategory',
        ),
        migrations.RemoveField(
            model_name='privatehospitalcategory',
            name='PrivateHospital',
        ),
        migrations.RemoveField(
            model_name='publichospital',
            name='HospitalCategory',
        ),
        migrations.RemoveField(
            model_name='publichospitalcategory',
            name='PublicHospital',
        ),
        migrations.AddField(
            model_name='privatehospital',
            name='PrivateHospitalCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PrivateHospitals', to='commerce.privatehospitalcategory'),
        ),
        migrations.AddField(
            model_name='publichospital',
            name='PublicHospitalCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PublicHospitals', to='commerce.publichospitalcategory'),
        ),
    ]