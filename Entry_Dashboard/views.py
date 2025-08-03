from django.shortcuts import render, HttpResponse

# Create your views here.
def Entery_Welcome_Dashboard_View(request):
    return render(request, 'Entry_Dashboard/Entry_Welcome_Dashboard.html')
