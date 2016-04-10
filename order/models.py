from django.db import models

# Create your models here.
BUSINESS = 'B'
PERSONAL = 'P'

residence_type_choices = (
    (BUSINESS, 'Business'),
    (PERSONAL, 'Personal'),
)

PERSONAL_ID = 'Pers'
PUBLIC_ID = 'Pub'

rating_id_choices = (
    (PERSONAL_ID, 'Personal ID'),
    (PUBLIC_ID, 'Public ID'),
)

INTERNATIONAL = 'I'
DOMESTIC = 'D'
shiping_type_choices = (
    (INTERNATIONAL, 'International'),
    (DOMESTIC, 'Domestic'),
)


class Locality(models.Model):
    country = models.CharField(max_length=20, blank=True, null=True)
    state = models.CharField(max_length=20, blank=True, null=True)
    title = models.CharField(max_length=20)
    postcode = models.CharField(max_length=10, blank=True, null=True)
    zone = models.CharField(max_length=4, blank=True, null=True)

    def __str__(self):
        return '%s_"%s"_"%s"' % (self.zone, self.title, self.postcode)


# ---------------------------
# TO USER MODEL
class RatingId(models.Model):
    id_type = models.CharField(max_length=4, choices=rating_id_choices, default=PUBLIC_ID)
    rating_id = models.CharField(max_length=8, default='00000000')
    rating_id.help_text = "Please use 8 digits key"
    # TODO add user unique id field association maybe add generator

    def __str__(self):
        return '"Name from User"_%s_%s' % (self.rating_id, self.id_type)
# ---------------------------


class CarrierService(models.Model):
    title = models.CharField(max_length=30)
    cube = models.IntegerField()
    service = models.CharField(max_length=30)
    zone_from = models.CharField(max_length=4)
    zone_from_postcode = models.CharField(max_length=10)
    zone_to = models.CharField(max_length=4)
    zone_to_postcode = models.CharField(max_length=10)

    def __str__(self):
        return '"%s"_"%s"_%s_"%s"_%s_"%s"_%s' % (
            self.title, self.service, self.cube,
            self.zone_from, self.zone_from_postcode,
            self.zone_to, self.zone_to_postcode
        )


class RatesTable(models.Model):
    calculation_method = models.CharField(max_length=15)
    rating_id = models.ForeignKey(RatingId, blank=True, null=True)
    carrier_service = models.ForeignKey(CarrierService, blank=True, null=True)
    fuel_surcharge = models.FloatField(default=0.0)
    surcharge_other_perc = models.FloatField(default=0.0)
    surcharge_flat = models.FloatField(default=0.0)
    tax_rate = models.FloatField(default=0.1)
    minimum = models.FloatField(default=0.0)
    break1_start = models.FloatField(default=0.0)
    break1_end = models.FloatField(default=0.0)
    basic1 = models.FloatField(default=0.0)
    kilo1 = models.FloatField(default=0.0)
    break2_start = models.FloatField(max_length=5, blank=True, null=True)
    break2_end = models.FloatField(max_length=5, blank=True, null=True)
    basic2 = models.FloatField(max_length=5, blank=True, null=True)
    kilo2 = models.FloatField(max_length=5, blank=True, null=True)
    break3_start = models.FloatField(max_length=5, blank=True, null=True)
    break3_end = models.FloatField(max_length=5, blank=True, null=True)
    basic3 = models.FloatField(max_length=5, blank=True, null=True)
    kilo3 = models.FloatField(max_length=5, blank=True, null=True)
    break4_start = models.FloatField(max_length=5, blank=True, null=True)
    break4_end = models.FloatField(max_length=5, blank=True, null=True)
    basic4 = models.FloatField(max_length=5, blank=True, null=True)
    kilo4 = models.FloatField(max_length=5, blank=True, null=True)
    break5_start = models.FloatField(max_length=5, blank=True, null=True)
    break5_end = models.FloatField(max_length=5, blank=True, null=True)
    basic5 = models.FloatField(max_length=5, blank=True, null=True)
    kilo5 = models.FloatField(max_length=5, blank=True, null=True)

    def __str__(self):
        return '%s_%s_%s' % (self.calculation_method, self.rating_id, self.carrier_service)


class Rate(models.Model):
    calculational_method = models.CharField(db_column='CALCULATIONAL_METHOD', max_length=15, blank=True, null=True)
    rating_category = models.CharField(db_column='RATING_CATEGORY', max_length=8, blank=True, null=True)
    cube = models.SmallIntegerField(db_column='CUBE', blank=True, null=True)
    carrier = models.CharField(db_column='CARRIER', max_length=20, blank=True, null=True)
    service = models.CharField(db_column='SERVICE', max_length=30, blank=True, null=True)
    sender_postcode = models.CharField(db_column='SENDER_POSTCODE', max_length=10, blank=True, null=True)
    zone_from = models.CharField(db_column='ZONE_FROM', max_length=4, blank=True, null=True)
    zone_from_desc = models.CharField(db_column='ZONE_FROM_DESC', max_length=20, blank=True, null=True)
    zone_to = models.CharField(db_column='ZONE_TO', max_length=4, blank=True, null=True)
    zone_to_desc = models.CharField(db_column='ZONE_TO_DESC', max_length=20, blank=True, null=True)
    receiver_postcode = models.CharField(db_column='RECEIVER_POSTCODE', max_length=10, blank=True, null=True)
    fuel_surcharge = models.TextField(db_column='FUEL_SURCHARGE', blank=True, null=True)
    surcharge_other_perc = models.TextField(db_column='SURCHARGE_OTHER_PERC', blank=True, null=True)
    surcharge_flat = models.TextField(db_column='SURCHARGE_FLAT', blank=True, null=True)
    minimum = models.TextField(db_column='MINIMUM', blank=True, null=True)
    break1_start = models.TextField(db_column='BREAK1_START', blank=True, null=True)
    break1_end = models.TextField(db_column='BREAK1_END', blank=True, null=True)
    basic1 = models.TextField(db_column='BASIC1', blank=True, null=True)
    kilo1 = models.TextField(db_column='KILO1', blank=True, null=True)
    break2_start = models.TextField(db_column='BREAK2_START', blank=True, null=True)
    break2_end = models.TextField(db_column='BREAK2_END', blank=True, null=True)
    basic2 = models.TextField(db_column='BASIC2', blank=True, null=True)
    kilo2 = models.TextField(db_column='KILO2', blank=True, null=True)
    break3_start = models.TextField(db_column='BREAK3_START', blank=True, null=True)
    break3_end = models.TextField(db_column='BREAK3_END', blank=True, null=True)
    basic3 = models.TextField(db_column='BASIC3', blank=True, null=True)
    kilo3 = models.TextField(db_column='KILO3', blank=True, null=True)
    break4_start = models.TextField(db_column='BREAK4_START', blank=True, null=True)
    break4_end = models.TextField(db_column='BREAK4_END', blank=True, null=True)
    basic4 = models.TextField(db_column='BASIC4', blank=True, null=True)
    kilo4 = models.TextField(db_column='KILO4', blank=True, null=True)
    break5_start = models.TextField(db_column='BREAK5_START', blank=True, null=True)
    break5_end = models.TextField(db_column='BREAK5_END', blank=True, null=True)
    basic5 = models.TextField(db_column='BASIC5', blank=True, null=True)
    kilo5 = models.TextField(db_column='KILO5', blank=True, null=True)

    def save(self, *args, **kwargs):
        super(Rate, self).save(*args, **kwargs)
        loc = Locality.objects.update_or_create(
            title=self.zone_from_desc,
            postcode=self.sender_postcode,
            zone=self.zone_from,
        )
        cs = CarrierService.objects.update_or_create(
            title=self.carrier,
            cube=self.cube,
            service=self.service,
            zone_from=self.zone_from,
            zone_from_postcode=self.sender_postcode,
            zone_to=self.zone_to,
            zone_to_postcode=self.receiver_postcode
        )
        cs_obj = CarrierService.objects.get(
            title=self.carrier,
            cube=self.cube,
            service=self.service,
            zone_from=self.zone_from,
            zone_from_postcode=self.sender_postcode,
            zone_to=self.zone_to,
            zone_to_postcode=self.receiver_postcode
        )
        rid = RatingId.objects.update_or_create(id_type=PUBLIC_ID, rating_id=self.rating_category)
        rid_obj = RatingId.objects.get(rating_id=self.rating_category)
        rt = RatesTable.objects.update_or_create(
            rating_id=rid_obj,
            carrier_service=cs_obj,
            calculation_method=self.calculational_method,
            fuel_surcharge=clean(self.fuel_surcharge),
            surcharge_other_perc=clean(self.surcharge_other_perc),
            surcharge_flat=clean(self.surcharge_flat),
            minimum=clean(self.minimum),
            break1_start=clean(self.break1_start),
            break1_end=clean(self.break1_end),
            basic1=clean(self.basic1),
            kilo1=clean(self.kilo1),
            break2_start=clean(self.break2_start),
            break2_end=clean(self.break2_end),
            basic2=clean(self.basic2),
            kilo2=clean(self.kilo2),
            break3_start=clean(self.break3_start),
            break3_end=clean(self.break3_end),
            basic3=clean(self.basic3),
            kilo3=clean(self.kilo3),
            break4_start=clean(self.break4_start),
            break4_end=clean(self.break4_end),
            basic4=clean(self.basic4),
            kilo4=clean(self.kilo4),
            break5_start=clean(self.break5_start),
            break5_end=clean(self.break5_end),
            basic5=clean(self.basic5),
            kilo5=clean(self.kilo5),
        )
        return


class Order(models.Model):
    customer_rating_id = models.ForeignKey(RatingId)

    # Customer Input - SKU Number and Shipment details
    sku = models.CharField(max_length=30)
    sku_description = models.CharField(max_length=30)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()
    status = models.CharField(max_length=10)

    # Customer Input - Sender Details
    sd_unit_apartment = models.CharField(max_length=30)
    sd_street_number = models.CharField(max_length=30)
    sd_street_name = models.CharField(max_length=30)
    sd_zone = models.ForeignKey(Locality, related_name='zone_from')

    sd_residence_type = models.CharField(max_length=1, choices=residence_type_choices, default=BUSINESS)

    # Customer Input - Receiver Details
    rc_unit_apartment = models.CharField(max_length=30)
    rc_street_number = models.CharField(max_length=30)
    rc_street_name = models.CharField(max_length=30)
    rc_zone = models.ForeignKey(Locality, related_name='zone_to')

    rc_residence_type = models.CharField(max_length=1, choices=residence_type_choices, default=BUSINESS)

    shipping_type = models.CharField(max_length=1, choices=shiping_type_choices, default=DOMESTIC)

    carrier_service = models.ForeignKey(CarrierService)

    price = models.FloatField()

    def get_rate_type(self):
        return '%s2%s' % (self.sd_residence_type, self.rc_residence_type)
    get_rate_type.short_description = 'Rate type'
    get_rate_type.allow_tags = True

    def get_cubic_weight(self):
        calc = (self.length * self.width * self.height) / 100
        return '%s' % calc
    get_cubic_weight.short_description = 'Cubic Weight'
    get_cubic_weight.allow_tags = True

    def get_order_status(self):
        return '%s' % self.status
    get_order_status.short_description = 'Order status'
    get_order_status.allow_tags = True

    def set_order_status(self, curent_state):
        self.status = curent_state
        return self.status

    def __str__(self):
        return self.sku


def clean(value):
    if value and value != "":
        return float(str(value).replace(',', '.'))
    return None