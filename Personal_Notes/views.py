from django.shortcuts import render

# Create your views here.
def Notes_Entry_Page(request):
    return render(request, 'Personal_Notes/Notes_Entry_Page.html')