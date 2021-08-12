from django.utils.safestring import mark_safe
from django import template

register = template.Library()

@register.filter
def colorize(val):
    mark = str(val)[:1]
    if mark == '-':
        html_string = f"<span style='color:green'><b>{val}</b></span>"
    elif mark == "0":
        html_string = f"<span style='color:blue'><b>{val}</b></span>"
    else: 
        html_string = f"<span style='color:red'><b>{val}</b></span>"

    return mark_safe(html_string)


