from django.shortcuts import render
from django.views.generic import TemplateView

from tree_menu.models import MenuItem


def menu_example_view(request):
    return render(request, 'tree_menu/index.html')


class MenuContentView(TemplateView):
    template_name = 'tree_menu/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_item = MenuItem.objects.get(url=self.request.path)
        context['content'] = menu_item.id
        return context
