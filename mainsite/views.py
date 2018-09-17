# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import redirect
from django.http import HttpResponse
from django.utils.crypto import random

from .models import Post
from datetime import datetime
from django.template.loader import get_template
from mainsite import models


# Create your views here.

# def homepage(request):
#     posts = Post.objects.all()
#     post_lists = list()
#     for count, post in enumerate(posts):
#         post_lists.append("No.{}:".format(str(count))+str(post)+"<br>")
#         post_lists.append("<small>"+str(post.body.encode('utf-8'))+"</small><br><br>")
#     return HttpResponse(post_lists)

def homepage_blog(request):
    template = get_template('index_blog.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost_blog(request, slug):
    template = get_template('post_blog.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')


def about_blog(request):
    template = get_template('about_blog.html')
    quotes = [
        'One','Two','Three','Four','Five'
    ]
    html = template.render({'quote': random.choice(quotes)})
    return HttpResponse(html)


def cell_index(request):
    products = models.Product.objects.all()
    template = get_template('index.html')
    html = template.render(locals())
    return HttpResponse(html)


def phone_details(request, id):
    try:
        product = models.Product.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    template = get_template('detail.html')
    html= template.render(locals())
    return HttpResponse(html)