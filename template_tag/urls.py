from django.contrib import admin
from django.urls import path

from tree_menu.views import menu_example

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', menu_example, name='menu-example'),
]
