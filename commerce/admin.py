from django.contrib import admin

from commerce.models import (HospitalType,DoctorType,PrivateHospital,PublicHospital,
    PublicHospitalCategory, PrivateHospitalCategory, PrivateDoctor,PublicDoctor,PublicDoctorCategory,PrivateDoctorCategory
)
"""class InlineProductImage(admin.TabularInline):
    model = ProductImage"""


"""class ProductAdmin(admin.ModelAdmin):
    inlines = [InlineProductImage,]
    list_display = ('id', 'name', 'qty', 'description', 'cost', 'price', 'discounted_price')
    list_filter = ('category', 'label', 'merchant', 'vendor')
    search_fields = ('name', 'qty', 'description', 'cost', 'price', 'discounted_price', 'merchant__name')
"""

admin.site.register(HospitalType)
admin.site.register(DoctorType)
admin.site.register(PublicHospital)
admin.site.register(PrivateHospital)
admin.site.register(PublicHospitalCategory)
admin.site.register(PrivateHospitalCategory)
admin.site.register(PrivateDoctor)
admin.site.register(PublicDoctor)
admin.site.register(PublicDoctorCategory)
admin.site.register(PrivateDoctorCategory)