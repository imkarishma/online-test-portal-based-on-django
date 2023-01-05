from django import template
register=template.Library()

@register.filter
def level_filter(value):
    value=int(value)
    if value>=0 or value<100:
       return 1
    
    elif value>=100 or value<200:
        return 2
    elif value>=200 or value<300:
        return 3
    elif value>=300 or value<400:
        return 4
