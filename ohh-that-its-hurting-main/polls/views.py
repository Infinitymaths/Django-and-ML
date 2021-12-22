from django.shortcuts import render, redirect
from . import final

# Create your views here.
def home(request):
    return render(request,"base.html")

def sentiment(request):
    res = ""
    if request.method == 'POST':
        if request.POST.get('pred_button'):
            name = request.POST['text data']
            res = final.pre(str(name))
            # print(res)
        else:
            redirect('home')
            res = ""
    else:
        print("Error Occurred")

    return render(request, "first.html", {'result': res})

def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")