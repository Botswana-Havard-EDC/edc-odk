from django.contrib import admin
from edc_model_admin import TabularInlineMixin, audit_fields

from .modeladmin_mixins import ModelAdminMixin
from ..admin_site import edc_odk_admin
from ..models import ConsentCopies
from ..models import (
    ConsentImage, SpecimenConsentImage)
from ..forms import ConsentCopiesForm
from ..forms import (
    ConsentImageForm, SpecimenConsentImageForm)


class ConsentImageInline(TabularInlineMixin, admin.TabularInline):
    model = ConsentImage
    form = ConsentImageForm
    extra = 0

    fields = ('consent_image', 'user_uploaded', 'datetime_captured',
              'modified', 'hostname_created',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = (
            'consent_image', 'datetime_captured', 'user_uploaded') + fields

        return fields


class SpecimenConsentImageInline(TabularInlineMixin, admin.TabularInline):
    model = SpecimenConsentImage
    form = SpecimenConsentImageForm
    extra = 0

    fields = ('specimen_consent_image', 'user_uploaded', 'datetime_captured',
              'modified', 'hostname_created',)

    def get_readonly_fields(self, request, obj=None):
        fields = super().get_readonly_fields(request, obj)
        fields = (
            'specimen_consent_image', 'datetime_captured', 'user_uploaded') + fields

        return fields


@admin.register(ConsentCopies, site=edc_odk_admin)
class ConsentCopiesAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = ConsentCopiesForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier', ]}),
        )

    list_display = ('subject_identifier', 'version', 'created', )

    inlines = [ConsentImageInline, SpecimenConsentImageInline]
