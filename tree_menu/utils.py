def build_menu_tree(menu_items):
    items_by_parent = {}

    for item in menu_items:
        parent_id = item.parent_id if item.parent else None
        items_by_parent.setdefault(parent_id, []).append(item)

    for items in items_by_parent.values():
        items.sort(key=lambda x: x.order)

    return items_by_parent
