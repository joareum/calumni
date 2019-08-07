from django.shortcuts import render, redirect, get_object_or_404
from .models import Cal,Comment
from django.utils import timezone
#from .form import BlogPost

# Create your views here.
def home(request):
    cals = Cal.objects.all()
    return render(request,"home.html", {'cals':cals})

def new(request):
    return render(request,'new.html')

def create(request):
     cal = Cal()
     cal.title = request.POST['cal_title']
     cal.apply = request.POST['cal_apply'] 
     cal.score = request.POST['cal_score']
     cal.cer = request.POST['cal_cer']
     cal.write = request.POST['cal_write']
     cal.body = request.POST['cal_body']
     cal.act = request.POST['cal_act']
     cal.schoolact = request.POST['cal_schoolact']
     cal.pub_date = timezone.datetime.now()
     cal.save()

     return redirect('home')

def read(request):
    cal = Cal.objects.all()
    return render(request, 'read.html',{'cal_posts':cal})

def detail(request, post_id):
    post = get_object_or_404(Cal, pk=post_id)
    return render(request, 'detail.html', {'post':post})

    #def blogpost(request):
    #if request.method == "POST"

    #else:
     #   form = BlogPost()
      #  return render(request, 'new.html', {'form':form})

def update(request, post_id):
     updated_post = get_object_or_404(Cal, pk=post_id)
     updated_post.title = request.POST['title']
     updated_post.body = ['body']
     updated_post.save()
     return redirect(''+ str(updated_post.id))

def renew(request, post_id):
     renew_post = get_object_or_404(Cal, pk=post_id)
     return render(request, 'renew.html', {'renew' : renew_post})

def delete(request, post_id):
     deleted_post = get_object_or_404(Cal, pk=post_id)
     deleted_post.delete()
     return redirect('')

def create_c(request, post_id):
     comment = Comment()
     comment.username = request.POST['comment_username']
     comment.body = request.POST['comment_body']
     comment.pub_date = timezone.datetime.now()
     comment.post = get_object_or_404(Cal, pk=post_id)
     comment.save()

     return redirect('read', post_id=post_id)