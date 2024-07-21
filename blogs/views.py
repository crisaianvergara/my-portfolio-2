from django.http import Http404
from django.shortcuts import render

from .utils import sort_list_of_dictionaries
from .odoo_api import OdooAPI

odoo_api = OdooAPI()

def index(request):
    posts = odoo_api.get_posts()
    posts.sort(key=sort_list_of_dictionaries)
    context = {"posts": posts, "title": "Blog"}
    return render(request, "blogs/index.html", context)

def detail(request, post_id):
    post = odoo_api.get_post(post_id)
    if not post:
        raise Http404("Post not found")
    context = {"post": post, "title": "Blog Detail"}
    return render(request, "blogs/detail.html", context)
