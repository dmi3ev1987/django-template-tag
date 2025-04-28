from django.shortcuts import render


def menu_example(request):
    return render(request, 'tree_menu/index.html')
