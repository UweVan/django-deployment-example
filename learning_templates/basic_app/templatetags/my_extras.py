from django import template

register = template.Library()

@register.filter(name='cut')
def cut(value,arg):
    """
    this cuts out of value of arg form string
    """

    return value.replace(arg,'')

# register.filter('cut',cut)
