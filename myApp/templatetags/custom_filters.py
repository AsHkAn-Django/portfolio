from django import template

register = template.Library()


@register.filter
def split(value, key):
    """
    Splits the string 'value' by the string 'key', handles None.
    Example: {{ value|split:"," }}
    """
    # Check if the value is None or an empty string
    if value is None:
        return []

    # Ensure it is treated as a string before splitting
    if not isinstance(value, str):
        value = str(value)

    return value.split(key)


@register.filter
def strip(value):
    # (Keep your existing strip function)
    if isinstance(value, str):
        return value.strip()
    return value
