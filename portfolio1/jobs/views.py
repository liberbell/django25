from django.shortcuts import render

# Create your views here.
def taro(request):
    return render(request, 'jobs/taro.html')

def home(request):
    return render(request, 'jobs/home.html')
