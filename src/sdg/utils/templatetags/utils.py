from django import template
from django.conf import settings
from django.utils.html import format_html

from sdg.producten.types import Language

register = template.Library()


class CaptureNode(template.Node):
    def __init__(self, nodelist, var_name):
        self.nodelist = nodelist
        self.var_name = var_name

    def render(self, context):
        output = self.nodelist.render(context)
        context[self.var_name] = output
        return ""


@register.tag
def capture(parser, token):
    """
    Captures contents and assigns them to variable.
    Allows capturing templatetags that don't support "as".

    Example:

        {% capture as body %}{% lorem 20 w random %}{% endcapture %}
        {% include 'components/text/text.html' with body=body only %}
    """
    args = token.split_contents()
    if len(args) < 3 or args[-2] != "as":
        raise template.TemplateSyntaxError(
            "'capture' tag requires a variable name after keyword 'as'."
        )
    var_name = args[-1]
    nodelist = parser.parse(("endcapture",))
    parser.delete_first_token()
    return CaptureNode(nodelist, var_name)


@register.simple_tag
def placekitten(width=800, height=600):
    """
    Renders a "placekitten" placeholder image.

    Example:

        {%placekitten %}
        {%placekitten 200 200 %}
    """
    return format_html('<img src="{}" />'.format(placekitten_src(width, height)))


@register.simple_tag
def placekitten_src(width=800, height=600):
    """
    Return a "placekitten" placeholder image url.

    Example:

        {% placekitten_src as src %}
        {% placekitten_src 200 200 as mobile_src %}
        {% include 'components/image/image.html' with mobile_src=mobile_src src=src alt='placekitten' only %}
    """
    return "//placekitten.com/{}/{}".format(width, height)


@register.simple_tag
def version():
    return settings.RELEASE


@register.filter(name="addclass")
def addclass(field, class_attr):
    return field.as_widget(attrs={"class": class_attr})


@register.simple_tag
def template_dir(value):
    return dir(value)


@register.inclusion_tag("forms/field.html")
def field(field, **kwargs):
    return {**kwargs, "field": field}


@register.inclusion_tag("forms/field_readonly.html")
def field_readonly(field, **kwargs):
    return {**kwargs, "field": field}


@register.inclusion_tag("forms/table_field.html")
def table_field(field, **kwargs):
    return {**kwargs, "field": field}


@register.inclusion_tag("forms/table_grid_field.html")
def table_grid_field(field, **kwargs):
    return {**kwargs, "field": field}


@register.inclusion_tag("forms/table_row.html")
def table_row(field, **kwargs):
    return {**kwargs, "field": field}


@register.inclusion_tag("forms/select.html")
def select(field, **kwargs):
    return {**kwargs, "field": field}


@register.inclusion_tag("forms/checkbox.html")
def checkbox(field, **kwargs):
    return {**kwargs, "field": field}


@register.inclusion_tag("forms/status_icon.html")
def status_icon(status, **kwargs):
    return {**kwargs, "status": status}
