from django.urls import path

from tree_menu.views import menu_example_view

urlpatterns = [
    path('', menu_example_view, name='menu-example'),
]
