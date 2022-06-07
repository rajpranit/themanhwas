from django.shortcuts import render ,redirect
from .models import AllPost ,Comment ,Categories

def index(request):
 
   allpost = AllPost.objects.all()
   sliderpost = AllPost.objects.filter(post_type = 'sliderpost')
   return render(request,'weebs/index.html',{
      'allpost':allpost,
      'sliderpost':sliderpost,
    })


def article_detail(request,pk ):
    
    posts = AllPost.objects.filter(pk = pk)
    count = 0
    for post in posts:
        for comment in post.comments.all():
            count += 1  


        
    return render(request,'weebs/article-detail.html',{
        "posts":posts,
        "count":count
    })

def comment(request,pk):
    if request.method == 'POST':
        posts = AllPost.objects.filter(pk = pk)
        for post in posts:
            post =post
            name = request.POST['cName']
            comment = request.POST['cMessage']
        comment = Comment(post = post,name=name,comment=comment)
        comment.save()

        return redirect('article-detail' ,pk)

def category(request):
    category = Categories.objects.all()

    return render(request,'weebs/category.html',{
        'category':category,
    })


def manhwa(request):
    post = AllPost.objects.filter(Type= 'manhwa' )
    return render(request,'weebs/manhwa.html',{
        "post":post,
    })


def manhua(request):
    post = AllPost.objects.filter(Type= 'manhua' )
    return render(request,'weebs/manhua.html',{
        "post":post,
    })

def search_content(request):
    if request.method == "POST":
        searched = request.POST["searched"]
        posts = AllPost.objects.filter( title__contains = searched)
        
    return render (request,'weebs/searched-content.html',{
        "posts":posts,
       
        "searched":searched,
    })


def about(request):
    return render(request,'weebs/about.html')



def contact(request):
    return render(request,'weebs/contact.html')
