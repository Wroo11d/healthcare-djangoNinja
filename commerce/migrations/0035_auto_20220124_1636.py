# Generated by Django 3.2.9 on 2022-01-24 13:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('commerce', '0034_auto_20220124_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivateDoctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='PrivateDoctors/', verbose_name='image')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('open_time', models.TimeField(blank=True, null=True, verbose_name='open_time')),
                ('close_time', models.TimeField(blank=True, null=True, verbose_name='close_time')),
                ('days', models.TextField(blank=True, null=True, verbose_name='days')),
                ('location', models.TextField(blank=True, null=True, verbose_name='location')),
                ('DoctorType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PrivateDoctors', to='commerce.doctortype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PrivateDoctorCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='PrivateDoctorCategories/', verbose_name='image')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublicDoctor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='PublicDoctors/', verbose_name='image')),
                ('name', models.CharField(blank=True, max_length=255, null=True, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('open_time', models.TimeField(blank=True, null=True, verbose_name='open_time')),
                ('close_time', models.TimeField(blank=True, null=True, verbose_name='close_time')),
                ('days', models.TextField(blank=True, null=True, verbose_name='days')),
                ('location', models.TextField(blank=True, null=True, verbose_name='location')),
                ('DoctorType', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PublicDoctors', to='commerce.doctortype')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PublicDoctorCategory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='PublicDoctorCategories/', verbose_name='image')),
                ('type', models.CharField(blank=True, max_length=255, null=True, verbose_name='type')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='PrivateHospitalCategory',
        ),
        migrations.RemoveField(
            model_name='hospital',
            name='PublicHospitalCategory',
        ),
        migrations.RemoveField(
            model_name='hospitalcategory',
            name='HospitalType',
        ),
        migrations.AlterField(
            model_name='publichospital',
            name='image',
            field=models.ImageField(upload_to='PublicHospitals/', verbose_name='image'),
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
        migrations.DeleteModel(
            name='DoctorCategory',
        ),
        migrations.DeleteModel(
            name='Hospital',
        ),
        migrations.DeleteModel(
            name='HospitalCategory',
        ),
        migrations.AddField(
            model_name='publicdoctor',
            name='PublicDoctorCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PublicDoctors', to='commerce.publicdoctorcategory'),
        ),
        migrations.AddField(
            model_name='privatedoctor',
            name='PrivateDoctorCategory',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='PrivateDoctors', to='commerce.privatedoctorcategory'),
        ),
    ]
