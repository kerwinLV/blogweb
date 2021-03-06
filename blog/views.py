import re

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from django.utils.text import slugify
import markdown
from markdown.extensions.toc import TocExtension

from .models import Post
# Create your views here.


def index(request):
    # return HttpResponse("欢迎访问我的官网")
    post_list = Post.objects.all().order_by('-created_time')
    context = {'post_list': post_list}
    return render(request,'blog/index.html',context=context)



def detail(request,pk):
    post= get_object_or_404(Post,pk=pk)
    md = markdown.Markdown(extensions=[
        'markdown.extensions.extra',
        'markdown.extensions.codehilite',
        # 记得在顶部引入 TocExtension 和 slugify
        TocExtension(slugify=slugify),
    ])
    post.body = md.convert(post.body)
    m = re.search(r'<div class="toc">\s*<ul>(.*)</ul>\s*</div>', md.toc, re.S)
    post.toc = m.group(1) if m is not None else ''
    return render(request,'blog/detail.html',context={'post':post})