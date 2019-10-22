from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/index.html')

def about(request):
    return render(request, 'pages/about.html')

def cart(request):
    return render(request, 'pages/cart.html')

def checkout(request):
    return render(request, 'pages/checkout.html')

def product(request):
    return render(request, 'pages/prodsingle.html')

def shop(request):
    return render(request, 'pages/shop.html')

def wishlist(request):
    return render(request, 'pages/wishlist.html')