
from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

def index(request):
    if request.method == "POST":
        title = request.POST.get("title")
        author = request.POST.get("author")
        details = request.POST.get("details")
        image_url = request.POST.get("image_url")

        Blog.objects.create(
            title=title,
            author=author,
            details=details,
            image_url=image_url
        )
        return redirect("/")


    blogs = Blog.objects.all().order_by("-date")
    return render(request, "index.html", {"blogs": blogs, "title": "My Blog"})


def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('/')
