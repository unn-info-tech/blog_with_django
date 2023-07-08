from django.http import HttpResponse
from django.shortcuts import render
from django.template.loader import get_template

from .forms import ContactForm
from blog.models import BlogPostModels

def home_page(request):
    qs = BlogPostModels.objects.all()[:2]
    context = {"title": "Welcome to UNN", "qs": qs}
    return render(request, "home.html", context)

def about(request):
    about = "I'm Abdulloh"
    return render(request, "about.html", {"title": about})

def contact(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        print("The name of data===================",form.cleaned_data)
        form = ContactForm()
    contact = "Something of mine 'CONTACT'"
    context = {
        "title": contact,
        "form": form
    }
    return render(request, "form.html",context)

def example(request):# Just an example how to render it with HttpResponse
    context = {"title": "something"}
    template_name = "hello_world.html"
    template_obj = get_template(template_name)
    render_item = template_obj.render(context)
    return HttpResponse(render_item)
    #return HttpResponse(get_template("hello_world.html").render({"title": "something"}))