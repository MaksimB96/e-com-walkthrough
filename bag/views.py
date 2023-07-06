from django.shortcuts import render

# Create your views here.


def view_bag(request):
    """
    View returns bag
    """
    return render(request, 'home/index.html')
