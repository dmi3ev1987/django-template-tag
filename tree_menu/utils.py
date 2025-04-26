from django.utils.html import escape
from django.utils.safestring import mark_safe


def build_menu_tree(menu_items):
    items_by_parent = {}

    for item in menu_items:
        parent_id = item.parent_id if item.parent else None
        items_by_parent.setdefault(parent_id, []).append(item)

    for items in items_by_parent.values():
        items.sort(key=lambda x: x.order)

    return items_by_parent


def render_menu(items_by_parent, active_items, current_path, parent_id=None, level=0):
    if parent_id not in items_by_parent:
        return ''

    items = items_by_parent[parent_id]
    menu_html = ['<ul>']

    for item in items:
        is_active = item.id in active_items
        has_active_child = any(child.id in active_items
                             for child in items_by_parent.get(item.id, []))

        show_children = (is_active and level < 1) or has_active_child

        item_name = escape(item.name)
        item_url = escape(item.get_url() or "#")

        menu_html.append(
            f'<li class="{"active" if is_active else ""}">'
            f'<a href="{item_url}">{item_name}</a>',
        )

        if show_children and item.id in items_by_parent:
            menu_html.append(
                render_menu(items_by_parent, active_items, current_path, item.id, level + 1),
            )

        menu_html.append('</li>')

    menu_html.append('</ul>')
    return mark_safe(''.join(menu_html))
