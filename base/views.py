from django.shortcuts import render
from django.http import HttpResponse
from .models import Portfolio, ProjectCategory, Member, Blog
from .forms import ContactForm


def home(request):
    projects = Portfolio.objects.all()
    categories = ProjectCategory.objects.all()
    return render(request,'home.html',{'projects':projects,'categories':categories})

def about(request):

    members = Member.objects.all()[:3]

    return render(request, 'about.html',{'members':members})

def portfolio(request):
    projects = Portfolio.objects.all()
    categories = ProjectCategory.objects.all()

    return render(request, 'portfolio.html',{'projects':projects,'categories':categories})

def portfolio_detail(request,pk):
    portfolio = Portfolio.objects.get(id=pk)

    return render(request, 'portfolio-detail.html',{'portfolio':portfolio})

def blog(request):
    blogs = Blog.objects.all()[:12]

    return render(request, 'blog-grid.html',{'blogs':blogs})

def blog_detail(request, pk):
    blog = Blog.objects.get(id=pk)
    return render(request, 'blog-single.html', {'blog':blog})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponse("<h1>Ma'lumotingiz jo'natildi</h1>")
    return render(request, 'contact.html',{'form':form})