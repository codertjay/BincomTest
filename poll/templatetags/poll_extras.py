from django import template

register = template.Library()
from ..models import Lga,PollingUnit


@register.filter(name='filter_lga_id')
def filter_lga_id(value):
    """Removes all values of arg from the given string"""
    try:
        lga_name = Lga.objects.get(lga_id=value).lga_name
    except:
        lga_name = None
    return value.replace(value, lga_name)


@register.filter(name='filter_polling_unit_id')
def filter_polling_unit_id(value):
    """Removes all values of arg from the given string"""
    try:
        polling_unit_name = PollingUnit.objects.get(uniqueid=value).polling_unit_name
    except:
        polling_unit_name = None
    return value.replace(value, polling_unit_name)
