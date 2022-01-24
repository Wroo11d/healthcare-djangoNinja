
import datetime

from ninja import Schema
from pydantic import UUID4
from django.contrib.auth import get_user_model

User=get_user_model()


"""class doctorIn(Schema):
    image : str
    name : str
    description : str
    open_time : datetime.time
    close_time : datetime.time
    days : str
    location : str
    #Doctor_category :

class doctorOut(Schema):
    id : UUID4
    image: str
    name: str
    description: str
    open_time: datetime.time
    close_time: datetime.time
    days: str
    location: str


class update_doctor(Schema):
    image: str
    name: str
    description: str
    open_time: datetime.time
    close_time: datetime.time
    days: str
    location: str

#########################################

class DcategoryIn(Schema):
    type : str
    image: str



class DcategoryOut(Schema):
    id : UUID4
    type: str
    image: str
    Doctors : list[doctorOut]


class update_Dcategory(Schema):
    type: str
    image: str
"""
#########################################

#######################################
"""class hospitalIn(Schema):
    image: str
    name: str
    location: str
    time: str
    days: str
    beds: int
    description: str




class hospitalOut(Schema):
    id:UUID4
    image: str
    name: str
    location: str
    time: str
    days: str
    beds: int
    description: str
    # Hospital_category :


class update_hospital(Schema):
    image: str
    name: str
    location: str
    time: str
    days: str
    beds: int
    description: str
    # Hospital_category :

"""
#############################################
class PublicDoctorIn(Schema):
    image : str
    name : str
    description : str
    open_time : datetime.time
    close_time : datetime.time
    days : str
    location : str
    #Doctor_category :

class PublicDoctorOut(Schema):
    id : UUID4
    image: str
    name: str
    description: str
    open_time: datetime.time
    close_time: datetime.time
    days: str
    location: str


class update_PublicDoctor(Schema):
    image: str
    name: str
    description: str
    open_time: datetime.time
    close_time: datetime.time
    days: str
    location: str

######################################3
class PrivateDoctorIn(Schema):
    image : str
    name : str
    description : str
    open_time : datetime.time
    close_time : datetime.time
    days : str
    location : str
    #Doctor_category :

class PrivateDoctorOut(Schema):
    id : UUID4
    image: str
    name: str
    description: str
    open_time: datetime.time
    close_time: datetime.time
    days: str
    location: str


class update_PrivateDoctor(Schema):
    image: str
    name: str
    description: str
    open_time: datetime.time
    close_time: datetime.time
    days: str
    location: str








######################################3
class publicHospitalIn(Schema):
    image: str
    name: str
    location: str
    time: str
    """open_time: datetime.time
    close_time: datetime.time"""
    days: str
    beds: int
    description: str




class publichospitalOut(Schema):
    id:UUID4
    image: str
    name: str
    location: str
    time: str
    """open_time: datetime.time
    close_time: datetime.time"""
    days: str
    beds: int
    description: str
    # Hospital_category :
###############################################

class privatehospitalIn(Schema):
    image: str
    name: str
    location: str
    time: str
    """open_time: datetime.time
    close_time: datetime.time"""
    days: str
    beds: int
    description: str




class privatehospitalOut(Schema):
    id:UUID4
    image: str
    name: str
    location: str
    time: str
    """open_time: datetime.time
    close_time: datetime.time"""
    days: str
    beds: int
    description: str
    # Hospital_category :
###############################################

"""class HcategoryIn(Schema):
    type: str
    image: str


class HcategoryOut(Schema):
    id: UUID4
    image: str
    type: str
    PublicHospitals:list[publichospitalOut]
  #  PrivateHospitals: list[privatehospitalOut]
    #Hospitals: list[hospitalOut]

class update_Hcategory(Schema):
    type: str
    image: str"""


#############################################

class HospitalTypeIn(Schema):
    image: str
    type: str


class HospitalTypeOut(Schema):
    id: UUID4
    image: str
    type: str
   # Hospitals: list[hospitalOut]

"""class HospitalTypeOut2(Schema):
  #  id: UUID4
  #  image: str
   # type: #str
  #HospitalCategories: list[HcategoryOut]
  # Hospitals: list[hospitalOut]"""

class update_HospitalType(Schema):
    image: str
    type: str
##################################3

class DoctorTypeIn(Schema):
    type : str
    image: str



class DoctorTypeOut(Schema):
    id : UUID4
    image: str
    type: str
   # Doctors : list[doctorOut]


class update_DoctorType(Schema):
    type: str
    image: str
######################################


class publicHospitalCategoryIn(Schema):
    image: str
    type: str

class publicHospitalCategoryOut(Schema):
    id: UUID4
    image: str
    type: str
    PublicHospitals: list[publichospitalOut]

######################################


class privateHospitalCategoryIn(Schema):
    image: str
    type: str

class privateHospitalCategoryOut(Schema):
    id: UUID4
    image: str
    type: str
    PrivateHospitals: list[privatehospitalOut]

######################################


class publicDoctorCategoryIn(Schema):
    image: str
    type: str

class publicDoctorCategoryOut(Schema):
    id: UUID4
    image: str
    type: str
    PublicDoctors: list[PublicDoctorOut]


######################################


class privateDoctorCategoryIn(Schema):
    image: str
    type: str

class privateDoctorCategoryOut(Schema):
    id: UUID4
    image: str
    type: str
    PrivateDoctors: list[PrivateDoctorOut]