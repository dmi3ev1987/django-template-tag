from django import template
from django.template.defaulttags import register as default_register
from django.template.loader import get_template

from tree_menu.models import MenuItem
from tree_menu.utils import build_menu_tree

register = template.Library()


@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    if not request:
        return ''

    current_path = request.path_info

    try:
        menu_items = MenuItem.objects.filter(
            menu_name=menu_name,
        ).select_related('parent')

        items_by_parent = build_menu_tree(menu_items)

        active_items = set()
        for item in menu_items:
            if item.is_active(current_path):
                active_items.add(item.id)
                parent = item.parent
                while parent:
                    active_items.add(parent.id)
                    parent = parent.parent

        template_name = 'tree_menu/menu.html'
        template = get_template(template_name)
        context = {
            'items_by_parent': items_by_parent,
            'active_items': active_items,
            'current_path': current_path,
        }
        # print("menu_items", menu_items)
        # print("context", context)
        return template.render(context)
    # Error handling - maybe need to add error message
    except ValueError:
        return ''


@default_register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
