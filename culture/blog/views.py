from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'pages/blog.html')

def single(request):
    return render(request, 'pages/single.html')