from django.shortcuts import render

# Home page view
def hi_view(request):
    return render(request, 'ThinkAi/home.html')

# About page view
def about_view(request):
    return render(request, 'ThinkAi/about.html')
