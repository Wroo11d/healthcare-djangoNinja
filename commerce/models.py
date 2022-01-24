import uuid

from PIL import Image
from django.contrib.auth import get_user_model
from django.db import models

from config.utils.models import Entity

#User = get_user_model()


"""class Doctor(Entity):
    image = models.ImageField('image', upload_to='Doctors/')
    name = models.CharField('name', null=True, blank=True, max_length=255)
    description = models.TextField('description', blank=True, null=True)
    open_time = models.TimeField('open_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    close_time = models.TimeField('close_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    days = models.TextField('days', null=True, blank=True)
    location = models.TextField('location', null=True, blank=True)
    DoctorType = models.ForeignKey('DoctorType', related_name='Doctors', null=True, blank=True, on_delete=models.CASCADE)
    DoctorCategory = models.ForeignKey('DoctorCategory', related_name='Doctors', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Hospital(Entity):
    image = models.ImageField('image', upload_to='Hospitals/')
    name = models.CharField('name', null=True, blank=True, max_length=255)
    location = models.TextField('location', null=True, blank=True)
    time = models.CharField('time', null=True, blank=True, max_length=255)

    days = models.TextField('days', null=True, blank=True)
    beds = models.IntegerField('beds', null=True, blank=True)
    description = models.TextField('description', blank=True, null=True)
    PublicHospitalCategory = models.ForeignKey('PublicHospitalCategory', related_name='Hospitals', null=True,
                                               blank=True, on_delete=models.CASCADE)
    PrivateHospitalCategory = models.ForeignKey('PrivateHospitalCategory', related_name='Hospitals', null=True,
                                               blank=True, on_delete=models.CASCADE)
    #HospitalType = models.ForeignKey('HospitalType', related_name='Hospitals', null=True, blank=True, on_delete=models.CASCADE)
    #HospitalCategory = models.ForeignKey('HospitalCategory', related_name='Hospitals', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name"""

class PublicDoctor(Entity):
    image = models.ImageField('image', upload_to='PublicDoctors/')
    name = models.CharField('name', null=True, blank=True, max_length=255)
    description = models.TextField('description', blank=True, null=True)
    open_time = models.TimeField('open_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    close_time = models.TimeField('close_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    days = models.TextField('days', null=True, blank=True)
    location = models.TextField('location', null=True, blank=True)
    DoctorType = models.ForeignKey('DoctorType', related_name='PublicDoctors', null=True, blank=True, on_delete=models.CASCADE)
    PublicDoctorCategory = models.ForeignKey('PublicDoctorCategory', related_name='PublicDoctors', null=True,
                                              blank=True,
                                              on_delete=models.CASCADE)
       #DoctorCategory = models.ForeignKey('DoctorCategory', related_name='Doctors', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PrivateDoctor(Entity):
    image = models.ImageField('image', upload_to='PrivateDoctors/')
    name = models.CharField('name', null=True, blank=True, max_length=255)
    description = models.TextField('description', blank=True, null=True)
    open_time = models.TimeField('open_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    close_time = models.TimeField('close_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    days = models.TextField('days', null=True, blank=True)
    location = models.TextField('location', null=True, blank=True)
    DoctorType = models.ForeignKey('DoctorType', related_name='PrivateDoctors', null=True, blank=True, on_delete=models.CASCADE)
    PrivateDoctorCategory = models.ForeignKey('PrivateDoctorCategory', related_name='PrivateDoctors', null=True,
                                               blank=True,
                                               on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class PublicHospital(Entity):
    image = models.ImageField('image', upload_to='PublicHospitals/')
    name = models.CharField('name', null=True, blank=True, max_length=255)
    location = models.TextField('location', null=True, blank=True)
    time = models.CharField('time', null=True, blank=True, max_length=255)
    """open_time = models.TimeField('open_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    close_time = models.TimeField('close_time', auto_now=False, auto_now_add=False, null=True, blank=True)"""
    days = models.TextField('days', null=True, blank=True)
    beds = models.IntegerField('beds', null=True, blank=True)
    description = models.TextField('description', blank=True, null=True)
    PublicHospitalCategory = models.ForeignKey('PublicHospitalCategory', related_name='PublicHospitals', null=True, blank=True,
       on_delete=models.CASCADE)
    #HospitalType = models.ForeignKey('HospitalType', related_name='Hospitals', null=True, blank=True, on_delete=models.CASCADE)
   # HospitalCategory = models.ForeignKey('HospitalCategory', related_name='PublicHospitals', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class PrivateHospital(Entity):
    image = models.ImageField('image', upload_to='Hospitals/')
    name = models.CharField('name', null=True, blank=True, max_length=255)
    location = models.TextField('location', null=True, blank=True)
    time = models.CharField('time', null=True, blank=True, max_length=255)
    """open_time = models.TimeField('open_time', auto_now=False, auto_now_add=False, null=True, blank=True)
    close_time = models.TimeField('close_time', auto_now=False, auto_now_add=False, null=True, blank=True)"""
    days = models.TextField('days', null=True, blank=True)
    beds = models.IntegerField('beds', null=True, blank=True)
    description = models.TextField('description', blank=True, null=True)
    PrivateHospitalCategory = models.ForeignKey('PrivateHospitalCategory', related_name='PrivateHospitals', null=True,
                                               blank=True,
                                               on_delete=models.CASCADE)
    #HospitalType = models.ForeignKey('HospitalType', related_name='Hospitals', null=True, blank=True, on_delete=models.CASCADE)
    #HospitalCategory = models.ForeignKey('HospitalCategory', related_name='PrivateHospitals', null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



"""class DoctorCategory(Entity):
    image = models.ImageField('image', upload_to='DoctorCategories/')
    type = models.CharField('type', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.type


class HospitalCategory(Entity):
    image = models.ImageField('image', upload_to='HospitalCategories/')
    type = models.CharField('type', null=True, blank=True, max_length=255)
    HospitalType = models.ManyToManyField('HospitalType', verbose_name='HospitalType',
                                          related_name='HospitalCategories', )

    def __str__(self):
        return self.type"""

class PublicDoctorCategory(Entity):
    image = models.ImageField('image', upload_to='PublicDoctorCategories/')
    type = models.CharField('type', null=True, blank=True, max_length=255)
    #PublicHospital = models.ForeignKey('PublicHospital', related_name='PublicHospitalCategories', null=True, blank=True,
                                      #   on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class PrivateDoctorCategory(Entity):
    image = models.ImageField('image', upload_to='PrivateDoctorCategories/')
    type = models.CharField('type', null=True, blank=True, max_length=255)

    #PrivateHospital = models.ForeignKey('PrivateHospital', related_name='PrivateHospitalCategories', null=True, blank=True,
                                     #  on_delete=models.CASCADE)
    #HospitalType = models.ManyToManyField('HospitalType', verbose_name='HospitalType',
                                         # related_name='HospitalCategories', )

    def __str__(self):
        return self.type



class PublicHospitalCategory(Entity):
    image = models.ImageField('image', upload_to='PublicHospitalCategories/')
    type = models.CharField('type', null=True, blank=True, max_length=255)
    #PublicHospital = models.ForeignKey('PublicHospital', related_name='PublicHospitalCategories', null=True, blank=True,
                                      #   on_delete=models.CASCADE)

    def __str__(self):
        return self.type

class PrivateHospitalCategory(Entity):
    image = models.ImageField('image', upload_to='PrivateHospitalCategories/')
    type = models.CharField('type', null=True, blank=True, max_length=255)

    #PrivateHospital = models.ForeignKey('PrivateHospital', related_name='PrivateHospitalCategories', null=True, blank=True,
                                     #  on_delete=models.CASCADE)
    #HospitalType = models.ManyToManyField('HospitalType', verbose_name='HospitalType',
                                         # related_name='HospitalCategories', )

    def __str__(self):
        return self.type


class HospitalType(Entity):
    image = models.ImageField('image', upload_to='HospitalTypes/')
    type = models.CharField('type', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.type


class DoctorType(Entity):
    image = models.ImageField('image', upload_to='DoctorTypes/')
    type = models.CharField('type', null=True, blank=True, max_length=255)

    def __str__(self):
        return self.type