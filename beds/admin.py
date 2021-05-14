from django.contrib import admin
from .models import Hospital, Patient, BedAllocation
# Register your models here.
admin.site.site_header = "COVID PORTAL"
admin.site.site_title = "COVID PORTAL"
admin.site.site_url = "/beds"

@admin.register(Hospital)
class HospitalAdmin(admin.ModelAdmin):
    fieldsets = (
    ( None, {
        'fields': ('name', 'location', 'district', 'phone', 'sector')
    }),
    ('Bed Information', {
        'fields': ('covid_beds', 'normal_beds', 'icu_beds', 'ventilator')
    }),
    )
    list_display = ('name', 'covid_beds', 'normal_beds', 'icu_beds', 'ventilator', 'total_beds')
    list_filter = ('location', 'district', 'sector')
    radio_fields = {"sector": admin.HORIZONTAL}
    ordering = ['name']
    search_fields = ['name', 'location']

    @admin.display(description='Total Beds')
    def total_beds(self, obj):
        total_beds = obj.covid_beds + obj.normal_beds + obj.icu_beds + obj.ventilator
        return total_beds


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'phone', 'category', 'status')
    search_fields = ['name', 'location']
    list_filter = ('location', 'district')

@admin.register(BedAllocation)
class BedAllocationAdmin(admin.ModelAdmin):
    raw_id_fields = ('patient', 'hospital')
    list_display = ('patient', 'hospital', 'category')

    def save_model(self, request, obj, form, change):
        patient = Patient.objects.get(pk=obj.patient.id)
        patient.status = 'A'
        patient.save()
        hospital = Hospital.objects.get(pk=obj.hospital.id)
        if obj.category == 'C':
            hospital.covid_beds = hospital.covid_beds - 1

        hospital.save()
        super().save_model(request, obj, form, change)
