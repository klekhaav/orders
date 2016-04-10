from django.contrib import admin
from import_export import resources, fields, widgets
from import_export.admin import ImportExportMixin
from import_export.widgets import DecimalWidget

from .models import *

# Register your models here.


class LocalityResource(resources.ModelResource):
    title = fields.Field(attribute='title', column_name='Sender_Locality')
    country = fields.Field(attribute='country', column_name='Sender_Country')
    postcode = fields.Field(attribute='postcode', column_name='Sender_Postcode')
    zone = fields.Field(attribute='zone', column_name='Zone_From')

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = Locality
        fields = ('title', 'country', 'postcode', 'zone')
        export_order = fields


class LocalityAdmin(ImportExportMixin, admin.ModelAdmin):
    fields = ['title', 'country', 'state', 'postcode', 'zone']
    list_display = ('title', 'country', 'state', 'postcode', 'zone')
    search_fields = ('title', 'country', 'state', 'postcode', 'zone')
    list_filter = ['title', 'country', 'state', 'postcode', 'zone']
    resource_class = LocalityResource


class RatingIdAdmin(admin.ModelAdmin):
    fields = ['rating_id', 'id_type']
    list_display = ('rating_id', 'id_type')
    search_fields = ('rating_id', 'id_type')
    list_filter = ['rating_id', 'id_type']


class CarrierServiceResources(resources.ModelResource):
    title = fields.Field(attribute='title', column_name='carrier')
    cube = fields.Field(attribute='cube', column_name='cube')
    service = fields.Field(attribute='service', column_name='service')
    zone_from = fields.Field(attribute='zone_from', column_name='zone_from')
    zone_to = fields.Field(attribute='zone_to', column_name='zone_to')

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = CarrierService
        fields = ('title', 'cube', 'service', 'zone_from', 'zone_to')
        export_order = fields


class CarrierServiceAdmin(admin.ModelAdmin):
    fields = ['title', 'service', 'cube', 'zone_from', 'zone_from_postcode', 'zone_to', 'zone_to_postcode']
    list_display = ('title', 'service', 'cube', 'zone_from', 'zone_from_postcode', 'zone_to', 'zone_to_postcode')
    search_fields = ('title', 'service', 'cube', 'zone_from', 'zone_from_postcode', 'zone_to', 'zone_to_postcode')
    list_filter = ['title', 'service', 'cube', 'zone_from', 'zone_from_postcode', 'zone_to', 'zone_to_postcode']
    resource_class = CarrierServiceResources


class RatesTableAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Basic Data',            {'fields':  ['calculation_method', 'rating_id']}),
        ('Carrier',               {'fields':  ['carrier_service',]}),
        ('Price Data',            {'fields':  ['tax_rate', 'minimum']}),
        ('Variable Data',         {'fields':  ['fuel_surcharge', 'surcharge_other_perc', 'surcharge_flat']}),
        ('Price_field#1',         {'fields':  ['break1_start', 'break1_end', 'basic1', 'kilo1']}),
        ('Price_field#2',         {'fields':  ['break2_start', 'break2_end', 'basic2', 'kilo2']}),
        ('Price_field#3',         {'fields':  ['break3_start', 'break3_end', 'basic3', 'kilo3']}),
        ('Price_field#4',         {'fields':  ['break4_start', 'break4_end', 'basic4', 'kilo4']}),
        ('Price_field#5',         {'fields':  ['break5_start', 'break5_end', 'basic5', 'kilo5']}),
    ]
    list_display = ('rating_id', 'carrier_service', 'tax_rate', 'minimum')
    search_fields = ('rating_id', 'carrier_service', 'tax_rate', 'minimum')
    list_filter = ['rating_id', 'carrier_service', 'tax_rate', 'minimum']


class RatesResource(resources.ModelResource):
    calculational_method = fields.Field(attribute='calculational_method', column_name='CALCULATIONAL_METHOD')
    rating_category = fields.Field(attribute='rating_category', column_name='RATING_CATEGORY')
    cube = fields.Field(attribute='cube', column_name='CUBE')
    carrier = fields.Field(attribute='carrier', column_name='CARRIER')
    service = fields.Field(attribute='service', column_name='SERVICE')
    sender_postcode = fields.Field(attribute='sender_postcode', column_name='SENDER_POSTCODE')
    zone_from = fields.Field(attribute='zone_from', column_name='ZONE_FROM')
    zone_from_desc = fields.Field(attribute='zone_from_desc', column_name='ZONE_FROM_DESC')
    zone_to = fields.Field(attribute='zone_to', column_name='ZONE_TO')
    zone_to_desc = fields.Field(attribute='zone_to_desc', column_name='ZONE_TO_DESC')
    receiver_postcode = fields.Field(attribute='receiver_postcode', column_name='RECEIVER_POSTCODE')
    fuel_surcharge = fields.Field(attribute='fuel_surcharge', column_name='FUEL_SURCHARGE')
    surcharge_other_perc = fields.Field(attribute='surcharge_other_perc', column_name='SURCHARGE_OTHER_PERC')
    surcharge_flat = fields.Field(attribute='surcharge_flat', column_name='SURCHARGE_FLAT')
    minimum = fields.Field(attribute='minimum', column_name='MINIMUM')
    break1_start = fields.Field(attribute='break1_start', column_name='BREAK1_START')
    break1_end = fields.Field(attribute='break1_end', column_name='BREAK1_END')
    basic1 = fields.Field(attribute='basic1', column_name='BASIC1')
    kilo1 = fields.Field(attribute='kilo1', column_name='KILO1')
    break2_start = fields.Field(attribute='break2_start', column_name='BREAK2_START')
    break2_end = fields.Field(attribute='break2_end', column_name='BREAK2_END')
    basic2 = fields.Field(attribute='basic2', column_name='BASIC2')
    kilo2 = fields.Field(attribute='kilo2', column_name='KILO2')
    break3_start = fields.Field(attribute='break3_start', column_name='BREAK3_START')
    break3_end = fields.Field(attribute='break3_end', column_name='BREAK3_END')
    basic3 = fields.Field(attribute='basic3', column_name='BASIC3')
    kilo3 = fields.Field(attribute='kilo3', column_name='KILO3')
    break4_start = fields.Field(attribute='break4_start', column_name='BREAK4_START')
    break4_end = fields.Field(attribute='break4_end', column_name='BREAK4_END')
    basic4 = fields.Field(attribute='basic4', column_name='BASIC4')
    kilo4 = fields.Field(attribute='kilo4', column_name='KILO4')
    break5_start = fields.Field(attribute='break5_start', column_name='BREAK5_START')
    break5_end = fields.Field(attribute='break5_end', column_name='BREAK5_END')
    basic5 = fields.Field(attribute='basic5', column_name='BASIC5')
    kilo5 = fields.Field(attribute='kilo5', column_name='KILO5')

    def get_instance(self, instance_loader, row):
        return False

    class Meta:
        model = Rate
        fields = (
            'calculational_method', 'rating_category', 'cube', 'carrier', 'service', 'sender_postcode',
            'zone_from', 'zone_from_desc', 'zone_to', 'zone_to_desc', 'receiver_postcode',
            'fuel_surcharge', 'surcharge_other_perc', 'surcharge_flat', 'minimum',
            'break1_start', 'break1_end', 'basic1', 'kilo1', 'break2_start', 'break2_end', 'basic2', 'kilo2',
            'break3_start', 'break3_end', 'basic3', 'kilo3', 'break4_start', 'break4_end', 'basic4', 'kilo4',
            'break5_start', 'break5_end', 'basic5', 'kilo5',
        )
        export_order = fields


class RatesAdmin(ImportExportMixin, admin.ModelAdmin):
    fields = (
        'calculational_method', 'rating_category', 'cube', 'carrier', 'service', 'sender_postcode',
        'zone_from', 'zone_from_desc', 'zone_to', 'zone_to_desc', 'receiver_postcode',
        'fuel_surcharge', 'surcharge_other_perc', 'surcharge_flat', 'minimum',
        'break1_start', 'break1_end', 'basic1', 'kilo1', 'break2_start', 'break2_end', 'basic2', 'kilo2',
        'break3_start', 'break3_end', 'basic3', 'kilo3', 'break4_start', 'break4_end', 'basic4', 'kilo4',
        'break5_start', 'break5_end', 'basic5', 'kilo5',
    )
    list_display = (
        'calculational_method', 'rating_category', 'cube', 'carrier', 'service', 'sender_postcode',
        'zone_from', 'zone_from_desc', 'zone_to', 'zone_to_desc', 'receiver_postcode',
        'fuel_surcharge', 'surcharge_other_perc', 'surcharge_flat', 'minimum',
        'break1_start', 'break1_end', 'basic1', 'kilo1', 'break2_start', 'break2_end', 'basic2', 'kilo2',
        'break3_start', 'break3_end', 'basic3', 'kilo3', 'break4_start', 'break4_end', 'basic4', 'kilo4',
        'break5_start', 'break5_end', 'basic5', 'kilo5',
    )
    search_fields = (
        'calculational_method', 'rating_category', 'cube', 'carrier', 'service', 'sender_postcode',
        'zone_from', 'zone_from_desc', 'zone_to', 'zone_to_desc', 'receiver_postcode',
        'fuel_surcharge', 'surcharge_other_perc', 'surcharge_flat', 'minimum',
        'break1_start', 'break1_end', 'basic1', 'kilo1', 'break2_start', 'break2_end', 'basic2', 'kilo2',
        'break3_start', 'break3_end', 'basic3', 'kilo3', 'break4_start', 'break4_end', 'basic4', 'kilo4',
        'break5_start', 'break5_end', 'basic5', 'kilo5',
    )
    list_filter = [
        'calculational_method', 'rating_category', 'cube', 'carrier', 'service', 'sender_postcode',
        'zone_from', 'zone_from_desc', 'zone_to', 'zone_to_desc', 'receiver_postcode',
        'fuel_surcharge', 'surcharge_other_perc', 'surcharge_flat', 'minimum',
    ]
    resource_class = RatesResource


class OrderAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Order',            {'fields':  ['sku', 'sku_description', 'shipping_type']}),
        ('Customer Info',    {'fields':  ['customer_rating_id', 'get_rate_type']}),
        ('Status',           {'fields':  ['carrier_service', 'price', 'status',]}),
        ('Parameters',       {'fields':  ['length', 'width', 'height', 'weight']}),
        ('Sender Details',   {'fields':  ['sd_unit_apartment', 'sd_street_number', 'sd_street_name',
                                         'sd_zone', 'sd_residence_type']}),
        ('Receiver Details', {'fields':  ['rc_unit_apartment', 'rc_street_number','rc_street_name',
                                          'rc_zone', 'rc_residence_type']}),
    ]
    list_display = ('sku', 'get_cubic_weight', 'customer_rating_id', 'get_order_status',
                    'sd_zone', 'rc_zone', 'get_rate_type')
    search_fields = ('sku', 'customer_rating_id', 'sd_zone', 'rc_zone')
    list_filter = ['customer_rating_id', 'sd_zone', 'rc_zone']
    readonly_fields = ('get_cubic_weight', 'get_order_status', 'get_rate_type')


admin.site.register(Locality, LocalityAdmin)
admin.site.register(CarrierService, CarrierServiceAdmin)
admin.site.register(RatingId, RatingIdAdmin)
admin.site.register(RatesTable, RatesTableAdmin)
admin.site.register(Rate, RatesAdmin)
admin.site.register(Order, OrderAdmin)
