from django.shortcuts import render


# Create your views here.
def index_view(request):
    context = {
        'animals': 'User AnimAls',
        'zoo_name': 'zoo name test',
    }
    return render(request, 'posts/index.html', context)

