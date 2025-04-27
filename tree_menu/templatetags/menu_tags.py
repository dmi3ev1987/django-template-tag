from django import template
from django.utils.html import escape
from ..models import MenuItem
from ..utils import build_menu_tree, render_menu

register = template.Library()

@register.simple_tag(takes_context=True)
def draw_menu(context, menu_name):
    request = context.get('request')
    if not request:
        return ''
    
    current_path = request.path_info
    
    try:
        menu_items = MenuItem.objects.filter(
            menu_name=menu_name
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
        
        return render_menu(
            items_by_parent=items_by_parent,
            active_items=active_items,
            current_path=current_path
        )
        
    except Exception as e:
        if settings.DEBUG:
            raise e
        return ''