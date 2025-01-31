from django import template
from django.conf import settings
from django.apps import apps



register = template.Library()


@register.simple_tag
def is_list(value):
    return isinstance(value, list)


@register.simple_tag
def settings_value(name, **kwargs):
    value = getattr(settings, name, None)
    if value and kwargs:
        return value.format(**kwargs)
    return value

@register.inclusion_tag("categories.html")
def list_ticket_categories():
    model = apps.get_model('uni_ticket', 'TicketCategory')
    category_objs = model.objects.filter(is_hidden=False, is_active=True).order_by("organizational_structure")
    structures = []
    name = ""
    category=None
    for category_obj in category_objs:
        if not name == category_obj.organizational_structure.name:
            name = category_obj.organizational_structure.name
            if not category is None:
                structures.append(category)
            category=dict()
            category["name"] = name
            category["categories"] = []
        category["categories"].append(category_obj.name)
    structures.append(category)
    return {"structures": structures}
        