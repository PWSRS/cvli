from django import template

register = template.Library()

@register.filter(name='add_class')
def add_class(field, css_class):
    return field.as_widget(attrs={"class": css_class})

@register.filter(name='add_error_class')
def add_error_class(field):
    if field.errors:
        return ' is-invalid'
    return ''
