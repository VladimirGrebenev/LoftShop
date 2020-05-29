from xml.etree import ElementTree as ET

from django import template
from django.utils.safestring import mark_safe

register = template.Library()


@register.filter(name="phone_to")
def phone_to(input_str):
    """
    Create link `tel:`
    """
    link_mailto = ET.Element("a", {"href": f"tel:{input_str}"})
    link_mailto.text = input_str
    return mark_safe(ET.tostring(link_mailto, encoding="unicode"))


# Or you can register tag like this
# register.filter("phone_to", phone_to)