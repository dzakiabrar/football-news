from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'npm' : '2306275241',
        'name': 'Dzaki Abrar',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)