from django.shortcuts import render

# Create your views here.
def show_data(request):
    return render(request, 'myapp/home.html')

def data(request):
    return render(request, 'myapp/show.html')