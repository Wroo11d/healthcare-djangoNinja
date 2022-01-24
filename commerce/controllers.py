from typing import List

from django.contrib.auth import get_user_model
from django.db.models import Q
from django.shortcuts import get_object_or_404
from ninja import Router
from account.authorization import GlobalAuth
from pydantic import UUID4

from commerce.models import *
from commerce.schemas import *
from config.utils.schemas import MessageOut

User = get_user_model()

commerce_controller = {'HospitalType':Router(tags=['HospitalType']),'DoctorType':Router(tags=['DoctorType']),
'PublicHospital':Router(tags=['PublicHospital']),'PrivateHospital':Router(tags=['PrivateHospital']),
                       'PublicHospitalCategory':Router(tags=['PublicHospitalCategory']), 'PrivateHospitalCategory':Router(tags=['PrivateHospitalCategory']),
                        'PublicDoctor':Router(tags=['PublicDoctor']),'PrivateDoctor':Router(tags=['PrivateDoctor']),
'PublicDoctorCategory':Router(tags=['PublicDoctorCategory']),'PrivateDoctorCategory':Router(tags=['PrivateDoctorCategory']),
                       }
##########################################################


"""@commerce_controller['Doctor'].get('Doctor',response={
     200:List[doctorOut],})
def list_doctors(request):
    dctr = Doctor.objects.all()
    return dctr



@commerce_controller['Doctor'].post('doctor',response={
     200: doctorOut,
     400: MessageOut
})
def create_doctor(request, payload: doctorIn):
    try:
        dctr = Doctor.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 200, dctr





@commerce_controller['Doctor'].get('doctor/{id}', response={
    200: doctorOut
})
def retrieve_doctor(request, id):
    return get_object_or_404(Doctor, id=id)


@commerce_controller['Doctor'].put('doctor/{id}', response={200: doctorOut})
def update_doctor(request, id: UUID4, payload: update_doctor):
    updatedctr = get_object_or_404(Doctor, id=id)
    for attr, value in payload.dict().items():
        setattr(updatedctr, attr, value)
    updatedctr.save()
    return updatedctr


@commerce_controller['Doctor'].delete('doctor/{id}')
def delete_doctor(request, id: UUID4):
    dctr = get_object_or_404(Doctor, id=id)
    dctr.delete()
    return 200, {'detail':'deleted'}


@commerce_controller['Doctor'].get('search', response={
    200:List[doctorOut],
    400:MessageOut})
def search(request, q: str = None):
    dctr =Doctor.objects.all()
    if q:
        dctr = dctr.filter(
            Q(name__icontains=q) | Q(description__icontains=q)

        )
    return dctr

######################################################

@commerce_controller['Hospital'].get('Hospital',response={
     200:List[hospitalOut],})
def list_hospitals(request):
    hspt = Hospital.objects.all()
    return hspt


@commerce_controller['Hospital'].post('hospital',response={
     200:hospitalOut,
     400: MessageOut
})
def create_hospirtal(request, payload: hospitalIn):
    try:
        hspt = Hospital.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 200, hspt

@commerce_controller['Hospital'].get('hospital/{id}', response={
    200: hospitalOut
})
def retrieve_hospital(request, id):
    return get_object_or_404(Hospital, id=id)


@commerce_controller['Hospital'].put('hospital/{id}', response={200: hospitalOut})
def update_hospital(request, id: UUID4, payload: update_hospital):
    updatedhspt = get_object_or_404(Hospital, id=id)
    for attr, value in payload.dict().items():
        setattr(updatedhspt, attr, value)
    updatedhspt.save()
    return updatedhspt


@commerce_controller['Hospital'].delete('hospital/{id}')
def delete_hospital(request, id: UUID4):
    hspt = get_object_or_404(Hospital, id=id)
    hspt.delete()
    return 200, {'detail':'deleted'}


@commerce_controller['Hospital'].get('look', response={
    200:List[hospitalOut],
    400:MessageOut})
def search_hospitals(request, q: str = None):
    hspt =Hospital.objects.all()
    if q:
        hspt = hspt.filter(
            Q(name__icontains=q) | Q(description__icontains=q)

        )
    return hspt





##########################################################
@commerce_controller['Categoryd'].get('Categoryd',response={
     200:List[DcategoryOut],})
def list_categories(request):
    hspt = DoctorCategory.objects.all()
    return hspt



@commerce_controller['Categoryd'].post('categoryd',response={
     200:DcategoryOut,
     400: MessageOut
})
def create_category(request, payload: DcategoryIn):
    try:
        hspt = DoctorCategory.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 200, hspt

@commerce_controller['Categoryd'].get('categoryd/{id}', response={
    200: DcategoryOut
})
def retrieve_category(request, id):
    return get_object_or_404(DoctorCategory, id=id)


@commerce_controller['Categoryd'].put('categoryd/{id}', response={200: DcategoryOut})
def update_category(request, id: UUID4, payload: update_Dcategory):
    updatedhspt = get_object_or_404(DoctorCategory, id=id)
    for attr, value in payload.dict().items():
        setattr(updatedhspt, attr, value)
    updatedhspt.save()
    return updatedhspt


@commerce_controller['Categoryd'].delete('categoryd/{id}')
def delete_category(request, id: UUID4):
    hspt = get_object_or_404(DoctorCategory, id=id)
    hspt.delete()
    return 200, {'detail':'deleted'}
#####################################################3

@commerce_controller['Categoryh'].get('Categoryh',response={
     200:List[HcategoryOut],})
def list_hcategories(request):
    hspt = HospitalCategory.objects.all()
    return hspt







@commerce_controller['Categoryh'].post('categoryh',response={
     200:HcategoryOut,
     400: MessageOut
})
def create_hcategory(request, payload: HcategoryIn):
    try:
        hspt = HospitalCategory.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 200, hspt

@commerce_controller['Categoryh'].get('categoryh/{id}', response={
    200: HcategoryOut
})
def retrieve_hcategory(request, id):
    return get_object_or_404(HospitalCategory, id=id)


@commerce_controller['Categoryh'].put('categoryh/{id}', response={200: HcategoryOut})
def update_hcategory(request, id: UUID4, payload: update_Hcategory):
    updatedhspt = get_object_or_404(HospitalCategory, id=id)
    for attr, value in payload.dict().items():
        setattr(updatedhspt, attr, value)
    updatedhspt.save()
    return updatedhspt


@commerce_controller['Categoryh'].delete('categoryh/{id}')
def delete_hcategory(request, id: UUID4):
    hspt = get_object_or_404(HospitalCategory, id=id)
    hspt.delete()
    return 200, {'detail':'deleted'}

"""

####################################################


@commerce_controller['HospitalType'].get('HospitalType',response={
     200:List[HospitalTypeOut],})
def list_types(request):
    hspt = HospitalType.objects.all()
    return hspt


"""@commerce_controller['HospitalType'].post('HospitalType',response={
     200:HospitalTypeOut,
     400: MessageOut
})
def create_type(request, payload: HospitalTypeIn):
    try:
        hspt = HospitalType.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 200, hspt"""

@commerce_controller['HospitalType'].get('HospitalType/{id}', response={
    200: HospitalTypeOut
})
def retrieve_type(request, id):
    return get_object_or_404(HospitalType, id=id)

"""
@commerce_controller['HospitalType'].put('HospitalType/{id}', response={200: HospitalTypeOut})
def update_category(request, id: UUID4, payload: update_HospitalType):
    updatedhspt = get_object_or_404(HospitalType, id=id)
    for attr, value in payload.dict().items():
        setattr(updatedhspt, attr, value)
    updatedhspt.save()
    return updatedhspt


@commerce_controller['HospitalType'].delete('HospitalType/{id}')
def delete_category(request, id: UUID4):
    hspt = get_object_or_404(HospitalType, id=id)
    hspt.delete()
    return 200, {'detail':'deleted'}"""

####################################################

@commerce_controller['DoctorType'].get('DoctorType',response={
     200:List[DoctorTypeOut],})
def list_types(request):
    hspt = DoctorType.objects.all()
    return hspt

@commerce_controller['DoctorType'].get('DoctorType/{id}', response={
    200: DoctorTypeOut
})
def retrieve_type(request, id):
    return get_object_or_404(DoctorType, id=id)



"""@commerce_controller['DoctorType'].post('DoctorType',response={
     200:DoctorTypeOut,
     400: MessageOut
})
def create_type(request, payload: DoctorTypeIn):
    try:
        hspt = DoctorType.objects.create(**payload.dict(), )
    except:
        return 400, {'detail': 'something wrong happened!'}

    return 200, hspt




@commerce_controller['DoctorType'].put('DoctorType/{id}', response={200: DoctorTypeOut})
def update_category(request, id: UUID4, payload: update_HospitalType):
    updatedhspt = get_object_or_404(DoctorType, id=id)
    for attr, value in payload.dict().items():
        setattr(updatedhspt, attr, value)
    updatedhspt.save()
    return updatedhspt


@commerce_controller['DoctorType'].delete('DoctorType/{id}')
def delete_category(request, id: UUID4):
    hspt = get_object_or_404(DoctorType, id=id)
    hspt.delete()
    return 200, {'detail':'deleted'}

"""

##############################################################
@commerce_controller['PublicHospital'].get('PublicHospital',response={
     200:List[publichospitalOut],})
def list_hospitals(request):
    hspt = PublicHospital.objects.all()
    return hspt


@commerce_controller['PublicHospital'].get('PublicHospital/{id}', response={
    200: publichospitalOut
})
def retrieve_type(request, id):
    return get_object_or_404(PublicHospital, id=id)

####################################################
@commerce_controller['PrivateHospital'].get('PrivateHospital',response={
     200:List[privatehospitalOut],})
def list_hospitals(request):
    hspt = PrivateHospital.objects.all()
    return hspt


@commerce_controller['PrivateHospital'].get('PrivateHospital/{id}', response={
    200: privatehospitalOut
})
def retrieve_type(request, id):
    return get_object_or_404(PrivateHospital, id=id)

##############################################################
@commerce_controller['PublicHospitalCategory'].get('PublicHospitalCategory',response={
     200:List[publicHospitalCategoryOut],})
def list_hospital(request):
    hspt = PublicHospitalCategory.objects.all()
    return hspt



@commerce_controller['PublicHospitalCategory'].get('PublicHospitalCategory/{id}', response={
    200: publicHospitalCategoryOut
})
def retrieve_type(request, id):
    return get_object_or_404(PublicHospitalCategory, id=id)


####################################################
@commerce_controller['PrivateHospitalCategory'].get('PrivateHospitalCategory',response={
     200:List[privateHospitalCategoryOut],})
def list_hospitalss(request):
    hspt = PrivateHospitalCategory.objects.all()
    return hspt


@commerce_controller['PrivateHospitalCategory'].get('PrivateHospitalCategory/{id}', response={
    200: privateHospitalCategoryOut
})
def retrieve_type(request, id):
    return get_object_or_404(PrivateHospitalCategory, id=id)

############################################
@commerce_controller['PublicDoctor'].get('PublicDoctor',response={
     200:List[PublicDoctorOut],})
def list_doctors(request):
    hspt = PublicDoctor.objects.all()
    return hspt


@commerce_controller['PublicDoctor'].get('PublicDoctor/{id}', response={
    200: PublicDoctorOut
})
def retrieve_type(request, id):
    return get_object_or_404(PublicDoctor, id=id)

####################################################
@commerce_controller['PrivateDoctor'].get('PrivateDoctor',response={
     200:List[PrivateDoctorOut],})
def list_hospitals(request):
    hspt = PrivateDoctor.objects.all()
    return hspt


@commerce_controller['PrivateDoctor'].get('PrivateDoctor/{id}', response={
    200: PrivateDoctorOut
})
def retrieve_type(request, id):
    return get_object_or_404(PrivateDoctor, id=id)

##############################################################
@commerce_controller['PublicDoctorCategory'].get('PublicDoctorCategory',response={
     200:List[publicDoctorCategoryOut],})
def list_hospital(request):
    hspt = PublicDoctorCategory.objects.all()
    return hspt



@commerce_controller['PublicDoctorCategory'].get('PublicDoctorCategory/{id}', response={
    200: publicDoctorCategoryOut
})
def retrieve_type(request, id):
    return get_object_or_404(PublicDoctorCategory, id=id)


####################################################
@commerce_controller['PrivateDoctorCategory'].get('PrivateDoctorHospitalCategory',response={
     200:List[privateDoctorCategoryOut],})
def list_hospitalss(request):
    hspt = PrivateDoctorCategory.objects.all()
    return hspt


@commerce_controller['PrivateDoctorCategory'].get('PrivateDoctorCategory/{id}', response={
    200: privateDoctorCategoryOut
})
def retrieve_type(request, id):
    return get_object_or_404(PrivateDoctorCategory, id=id)