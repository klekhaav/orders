from django import forms
from .models import residence_type_choices, shiping_type_choices, Order, Locality


class OrderCarrierSelectorForm(forms.ModelForm):
    field_order = ['sku', 'sku_description', 'length', 'width', 'height', 'weight', 'sd_zone', 'rc_zone']

    class Meta:
        model = Order
        fields = ['sku', 'sku_description', 'length', 'width', 'height', 'weight', 'sd_zone', 'rc_zone']


class OrderCustomerInput(forms.Form):
    # Customer Input - Sender Details
    sd_unit_apartment = forms.CharField()
    sd_street_number = forms.CharField()
    sd_street_name = forms.CharField()
    sd_residence_type = forms.ChoiceField(choices=residence_type_choices)

    # Customer Input - Receiver Details
    rc_unit_apartment = forms.CharField()
    rc_street_number = forms.CharField()
    rc_street_name = forms.CharField()
    rc_residence_type = forms.ChoiceField(choices=residence_type_choices)

    shipping_type = forms.ChoiceField(choices=shiping_type_choices)

    def get_payment_system_list(self):
        pass
