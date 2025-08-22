from django.shortcuts import render, HttpResponse

# Create your views here.
def Entery_Welcome_Dashboard_View(request):
    return render(request, 'Entry_Dashboard/Entry_Welcome_Dashboard.html')

def Registration_View(request):
    return render(request, 'Entry_Dashboard/Registeration_Page.html')

def Login_View(request):
    return render(request, 'Entry_Dashboard/Login_Page.html')


# C:\Users\vasudev pareek\Desktop\Doify\Entry_Dashboard\templates\Entry_Dashboard\Registeration_Page.html