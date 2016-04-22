from .models import *
from rest_framework import serializers
import django_filters


class LocalitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Locality
        fields = ('title', 'state', 'country', 'postcode', 'zone')


class CarrierServiceSerializer(serializers.ModelSerializer):

    class Meta:
        model = CarrierService
        fields = ('title', 'cube', 'service', 'zone_from', 'zone_from_postcode', 'zone_to', 'zone_to_postcode')


class RatingIdSerializer(serializers.ModelSerializer):
    id_type = serializers.ChoiceField(rating_id_choices)
    rating_id = serializers.CharField(max_length=8)

    class Meta:
        model = RatingId
        fields = ('id_type', 'rating_id')

    def create(self, validated_data):
        return RatingId.objects.create(**validated_data)

    def update(self, instance, validated_data):
        id_type = validated_data.get('id_type', instance.type)
        rating_id = validated_data.get('rating_id', instance.rating_id)
        instance.save()
        return instance


class RateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rate
        fields = (
            'calculational_method', 'rating_category', 'cube', 'carrier', 'service', 'sender_postcode', 'zone_from',
            'zone_from_desc', 'zone_to', 'zone_to_desc', 'receiver_postcode', 'fuel_surcharge', 'surcharge_other_perc',
            'surcharge_flat', 'minimum', 'break1_start', 'break1_end', 'basic1', 'kilo1', 'break2_start', 'break2_end',
            'basic2', 'kilo2', 'break3_start', 'break3_end', 'basic3', 'kilo3', 'break4_start', 'break4_end', 'basic4',
            'kilo4', 'break5_start', 'break5_end', 'basic5', 'kilo5'
        )


class RatesTableSerializer(serializers.ModelSerializer):
    carrier_service = CarrierServiceSerializer(many=False)
    rating_id = RatingIdSerializer(many=False)

    class Meta:
        model = RatesTable
        fields = (
            'calculation_method', 'rating_id', 'carrier_service', 'fuel_surcharge', 'surcharge_other_perc',
            'surcharge_flat', 'tax_rate', 'minimum', 'break1_start', 'break1_end', 'basic1', 'kilo1', 'break2_start',
            'break2_end', 'basic2', 'kilo2', 'break3_start', 'break3_end', 'basic3', 'kilo3', 'break4_start',
            'break4_end', 'basic4', 'kilo4', 'break5_start', 'break5_end', 'basic5', 'kilo5'
        )


class OrderSerializer(serializers.ModelSerializer):
    customer_rating_id = RatingIdSerializer(many=False)
    sd_zone = LocalitySerializer(many=False)
    rc_zone = LocalitySerializer(many=False)
    sd_residence_type = serializers.ChoiceField(residence_type_choices)
    rc_residence_type = serializers.ChoiceField(residence_type_choices)
    sku = serializers.CharField(max_length=30)
    sku_description = serializers.CharField(max_length=100)
    length = serializers.FloatField()
    width = serializers.FloatField()
    height = serializers.FloatField()
    weight = serializers.FloatField()
    status = serializers.CharField(max_length=10)
    sd_addr0 = serializers.CharField(max_length=30)
    sd_addr1 = serializers.CharField(max_length=30)
    sd_addr2 = serializers.CharField(max_length=30)
    sd_addr3 = serializers.CharField(max_length=30)
    rc_addr0 = serializers.CharField(max_length=30)
    rc_addr1 = serializers.CharField(max_length=30)
    rc_addr2 = serializers.CharField(max_length=30)
    rc_addr3 = serializers.CharField(max_length=30)
    carrier_service = CarrierServiceSerializer(many=False)
    price = serializers.FloatField()

    class Meta:
        model = Order
        fields = (
            'customer_rating_id', 'sku', 'sku_description', 'length', 'width', 'height', 'weight', 'status',
            'sd_addr0', 'sd_addr1', 'sd_addr2', 'sd_addr3', 'sd_zone', 'sd_residence_type',
            'rc_addr0', 'rc_addr1', 'rc_addr2', 'rc_addr3', 'rc_zone', 'rc_residence_type', 'shipping_type',
            'carrier_service', 'price', 'manifest'
        )

    def create(self, validated_data):

        customer_rating_id_data = validated_data.pop('customer_rating_id')
        sd_zone_data = validated_data.pop('sd_zone')
        rc_zone_data = validated_data.pop('rc_zone')
        carrier_service_data = validated_data.pop('carrier_service')
        cs = CarrierService.objects.create(**carrier_service_data)
        cri = RatingId.objects.create(**customer_rating_id_data)
        sd_zone = Locality.objects.create(**sd_zone_data)
        rc_zone = Locality.objects.create(**rc_zone_data)

        print(sd_zone_data)

        order = Order.objects.create(
            customer_rating_id=cri,
            sd_zone=sd_zone,
            rc_zone=rc_zone,
            carrier_service=cs,
            **validated_data
        )
        return order

    def update(self, instance, validated_data):
        customer_rating_id = validated_data.get('customer_rating_id', instance.RatingId)
        sd_zone = validated_data.get('sd_zone', instance.sd_zone)
        rc_zone = validated_data.get('rc_zone', instance.rc_zone)
        sd_residence_type = validated_data.get('sd_residence_type', instance.sd_residence_type)
        rc_residence_type = validated_data.get('rc_residence_type', instance.rc_residence_type)
        sku = validated_data.get('sku', instance.sku )
        sku_description = validated_data.get('sku_description', instance.sku_description)
        length = validated_data.get('length', instance.length)
        width = validated_data.get('width', instance.width)
        height = validated_data.get('height', instance.height)
        weight = validated_data.get('weight', instance.weight)
        status = validated_data.get('status', instance.status)
        sd_addr0 = validated_data.get('sd_addr0', instance.sd_addr0)
        sd_addr1 = validated_data.get('sd_addr1', instance.sd_addr1)
        sd_addr2 = validated_data.get('sd_addr2', instance.sd_addr2)
        sd_addr3 = validated_data.get('sd_addr3', instance.sd_addr3)
        rc_addr0 = validated_data.get('rc_addr0', instance.rc_addr0)
        rc_addr1 = validated_data.get('rc_addr1', instance.rc_addr1)
        rc_addr2 = validated_data.get('rc_addr2', instance.rc_addr2)
        rc_addr3 = validated_data.get('rc_addr3', instance.rc_addr3)
        carrier_service = validated_data.get('rc_street_name', instance.carrier_service)
        price = validated_data.get('rc_street_name', instance.price)
        instance.save()
        return instance
