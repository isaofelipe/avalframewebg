from django import template
register = template.Library()

@register.simple_tag
def porcentagem(value):
    if value != None:
        return "{0:.00f}%".format(value*100)
    else:
        return ""