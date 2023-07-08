from django.shortcuts import render, get_object_or_404, redirect
from django.http import Http404
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.
from .models import BlogPostModels
from .forms import BlogPostModelForm

#  GET -> 1 object
# filter -> [] objects

"""
def blog(request, slugme):
    print("Django says:", request.method, request.path, request.user)
    """"""try:
        obj = BlogPost.objects.get(id=idme) # query -> database -> data -> django renders it
    except:
        raise Http404""""""
    obj = get_object_or_404(BlogPost, slugModels=slugme)
    #obj = get_object_or_404(BlogPost, id = idme)
    #querysetme = BlogPost.objects.filter(slugModels=slugme)
    #obj = querysetme[1]
    titleme = "blog.html"
    belowme = {"object": obj}
    return render(request, titleme, belowme)"""


# GET -> Retrive/ list
# POST -> Create/Update/Delete
# CRUD - All in one - Create/Retrieve/Update/Delete

def blog_post_list_view(request):
    # list out object
    # could be search
    qs = BlogPostModels.objects.all() # queryset -> list of python objects
    titleme = "blog/list.html"
    belowme = {"object_listme": qs}
    return render(request, titleme, belowme)

@staff_member_required
def blog_post_create_view(request):
    # create objects
    # ? use form
    formme = BlogPostModelForm(request.POST or None)
    if formme.is_valid():
        print(formme.cleaned_data)
        obj = formme.save(commit=False)
        obj.user = request.user
        obj.save()
        formme = BlogPostModelForm()
    templateme = "form.html"
    belowme = {"form": formme}
    return render(request, templateme, belowme)

@staff_member_required
def blog_post_detail_view(request, slugme): # retrieve
    # 1 object or detail view
    obj = get_object_or_404(BlogPostModels, slugModels=slugme)
    templateme = "blog/detail.html"
    contextme = {"object": obj}
    return render(request, templateme, contextme)

@staff_member_required
def blog_post_update_view(request, slugme):
    obj = get_object_or_404(BlogPostModels, slugModels=slugme)
    formme = BlogPostModelForm(request.POST or None, instance=obj)
    if formme.is_valid():
        formme.save()
    templateme = "form.html"
    contextme = {"title": f"Update - '{obj.titleModels}'", "form": formme}
    return render(request, templateme, contextme)

@staff_member_required
def blog_post_delete_view(request, slugme):
    obj = get_object_or_404(BlogPostModels, slugModels=slugme)
    templateme = "blog/delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect("/blogs")
    contextme = {"object_list": obj, "title": obj.titleModels}
    return render(request, templateme, contextme)
