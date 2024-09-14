from django.shortcuts import render

# def home(request):
#     return render(request, 'home.html')
def home(request):
    context = {
        'greeting': 'Hello, welcome to my website!'
    }
    return render(request, 'home.html', context)

