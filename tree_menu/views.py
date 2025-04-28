from django.shortcuts import render


def menu_example_view(request):
    return render(request, 'tree_menu/index.html')
