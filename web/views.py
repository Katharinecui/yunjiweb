import markdown

from django.shortcuts import render, get_object_or_404
from .models import Post, Category 
from django.views.generic import ListView # 类视图函数

# Create your views here.
 
def index(request):
    post_list = Post.objects.all().order_by('-created_time')
    return render(request, 'web/index.html', context={'post_list': post_list})

def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body, extensions=['markdown.extensions.extra', 'markdown.extensions.codehilite',
                                                        'markdown.extensions.toc',])
    return render(request, 'web/detail.html', context={'post': post})

def aboutus(request):
    return render(request, 'web/aboutus.html')

def aboutrange(request):
    return render(request, 'web/aboutrange.html')

def aboutyunji(request):
    return render(request, 'web/aboutyunji.html')

def service(request):
    return render(request, 'web/service.html')

def sereva(request):
    return render(request, 'web/sereva.html')

def serproduction(request):
    return render(request, 'web/serproduction.html')

def serask(request):
    return render(request, 'web/serask.html')

def serdes(request):
    return render(request, 'web/serdes.html')

"""def category(request, pk): 
    # 成功案例、新闻资讯、文件下赞、项目公示的单页
    cate = get_object_or_404(Category, pk=pk)
    post_list = Post.objects.filter(category=cate).order_by('-created_time')
    return render(request, 'web/category.html', context={'post_list': post_list})"""

class CategoryView(ListView):
    model = Post
    template_name = 'web/category.html'
    context_object_name = 'post_list'
    # 指定 paginate_by 属性后开启分页功能，其值代表每一页包含多少篇文章
    paginate_by = 10

    def get_queryset(self):
        cate = get_object_or_404(Category, pk=self.kwargs.get('pk'))
        return super(CategoryView, self).get_queryset().filter(category=cate).order_by('-created_time')

def contact(request):
    return render(request, 'web/contact.html')