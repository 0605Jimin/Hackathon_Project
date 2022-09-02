from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import PostForm, CommentForm
from .models import Post
from django.views.generic import DetailView
from django.contrib.auth.decorators import login_required

# def photo_list(request):
#     return render(request, 'photolist/photo_list.html')

def photo_list(request): 
    qs = Post.objects.all()
    q = request.GET.get('q', '')
    if q:
        qs = qs.filter(title__icontains=q)
    # instagram/templates/instagram/post_list.html
    return render(request, 'photolist/photo_list.html', {
        'photo_list': qs,
        'q': q ,
    })

# class PostDetailView(DetailView):
#     template_name = 'photolist/photo_detail.html'
#     model = Post
#     comment_form = CommentForm()
#     # queryset = Post.objects.filter(is_public=True)

#     def get_queryset(self):
#         qs = super().get_queryset()
#         if not self.request.user.is_authenticated:
#             qs = qs.filter(is_public=True)
#         return qs

# photo_detail = PostDetailView.as_view()

def photo_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comment_form = CommentForm()
    return render(request, "photolist/photo_detail.html", {
        "post": post,
        "comment_form": comment_form,
    })


@login_required
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if post.author != request.user:
        messages.error(request, '작성자만 수정할 수 있습니다.')
        return redirect(post)

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save()
            messages.success(request, '포스팅을 수정했습니다.')
            return redirect(post)

    else:
        form = PostForm(instance=post)

    return render(request, 'photolist.post_form.html', {
        'form': form,
        'post': post,
    })

@login_required
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if post.author != request.user:
        messages.error(request, '작성자만 삭제할 수 있습니다.')
        return render(request, 'photolist/post_confirm_delete.html', {
            'post' : post,
        })


def home(request):
    return render(request, 'photolist/home.html')

def account(request):
    return render(request, 'photolist/account.html')


#def post_new(request):
    # if request.method == 'POST':
    #     form = PostForm(request.POST, request.FILES)
    #     if form.is_valid():
    #         post = form.save(commit=False)
    #         post.save()
    #         messages.success(request, '포스팅을 저장했습니다.')
    #         return redirect(post)
    #     else:
    #         form = PostForm()

    #     return render(request, 'photolist/post_form.html', {
    #         'form': form,
    #         'post': None
    #     })
    #form = PostForm()
    #return render(request, 'photolist/post_form.html', {
    #    'form': form
    #})

@login_required
def post_new(request):
    if request.method == 'POST' or request.method == 'FILES':
        # 입력 내용을 DB에 저장
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            # 저장하라
            form.save()
            messages.success(request, "정상적으로 포스팅 되었습니다.")
            return redirect('photolist:photo_list')
    else:
        # 입력을 받을 수 있는 html을 갖다주기
        form = PostForm() #객체 만들어주기
    return render(request, 'photolist/post_form.html', {
        'form': form,
        })
#.
def detail(request, blog_id):
    # blog_id 번째 블로그 글을 데이터베어스로부터 갖고와서
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    # blog_id 번째 블로그 글을 detail.html로 띄어주는 코드
    comment_form = CommentForm()

@login_required
def post_like(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like_user_set.add(request.user)
    messages.success(request, f"포스팅#{post.pk}의 좋아요를 취소합니다.")
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)

@login_required
def post_unlike(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.like_user_set.remove(request.user)
    messages.success(request, f"포스팅#{post.pk}를 좋아합니다.") 
    redirect_url = request.META.get("HTTP_REFERER", "root")
    return redirect(redirect_url)

@login_required
def comment_new(request,post_pk):
    post = get_object_or_404(Post, pk=post_pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect(comment.post)
    else:
        form = CommentForm()
    return render(request, "photolist/comment_form.html", {"form":form})