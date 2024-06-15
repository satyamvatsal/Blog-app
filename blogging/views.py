from django.shortcuts import render,redirect
from django.http import Http404,JsonResponse
from django.template import loader
from django.utils import timezone
# Create your views here.
from .models import post,comment


def index(request):
    if(post.objects.all().count() == 0):
        return render(request,"index.html")
    
    latest_post_list = post.objects.all().order_by("-pub_date")
    latest_postId = post.objects.latest('id').id
    context = {
        "latest_post_list":latest_post_list,
        "latest_post_id":latest_postId,
    }
    return render(request,"index.html",context)

def post_detail(request,id):
    try:
        pst=post.objects.get(pk=id)
    except post.DoesNotExist:
        raise Http404("The requested post does not exist.")
    latest_postId = post.objects.latest('id').id
    comments = reversed(list(comment.objects.all().filter(post = pst)))
    context = {
        "title":pst.title,
        "post_id":pst.id,
        "content":pst.content,
        "date":pst.pub_date,
        "latest_post_id":latest_postId,
        "comments":comments,
    }
    return render(request,"detail-post.html",context)
def about(request):
    latest_postId = post.objects.latest('id').id
    
    return render(request,"about.html",{"latest_post_id":latest_postId})

def submit_comment(request,id):
    if request.method == 'POST':
        Post = post.objects.get(pk=id)
        username = request.POST['username']
        comment_text = request.POST.get('comment_text')
        new_comment = comment(post= Post,username=username, comment_text=comment_text)
        new_comment.save()
        return JsonResponse({'status': 'success', 'message': 'Comment submitted successfully!'})
    return JsonResponse({'status': 'error', 'message': 'Invalid request'})