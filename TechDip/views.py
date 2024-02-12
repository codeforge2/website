from django.shortcuts import render
from django.http import HttpResponse
from .models import dev_group

# Create your views here.
def about_us(request):
    my_data = dev_group.objects.all()
    return render(request, "TechDip/AI-html-1.0.0/index.html", {"data": my_data}) 