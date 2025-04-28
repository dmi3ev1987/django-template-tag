from django.urls import path, re_path

from tree_menu.views import MenuContentView, menu_example_view

urlpatterns = [
    path('', menu_example_view, name='menu-example'),
    re_path(
        r'^(?P<menu_section>.+)/$',
        MenuContentView.as_view(),
        name='menu-item-view',
    ),
]
