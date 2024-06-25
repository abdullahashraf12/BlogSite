from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Post, Comment ,Tag ,Category
from .forms import PostForm, CommentForm
from .serializers import PostSerializer, CategorySerializer, TagSerializer, CommentSerializer
# views.py
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly  # Import custom permission
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListCreateAPIView
from .custom_pagination import CustomPagination
from rest_framework.generics import ListCreateAPIView
from django.db.models import Prefetch
from userauths.models import Profile
# Create your views here.
import time
def home(request):
    # Fetch all posts and prefetch related categories and tags
    posts = Post.objects.prefetch_related(
        Prefetch('categories', queryset=Category.objects.all(), to_attr='post_categories'),
        Prefetch('tags', queryset=Tag.objects.all(), to_attr='post_tags')
    ).all()

    # Fetch other required data
    comments = Comment.objects.all()
    categories = Category.objects.all()
    tags = Tag.objects.all()

    context = {
        'posts': posts,
        'comments': comments,
        'categories': categories,
        'tags': tags,
    }
    print(posts.values('categories', 'tags'))


    return render(request, 'index.html', context)



# @login_required
def create_post(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                post = form.save(commit=False)
                post.author = request.user.profile  # Assign the Profile instance of the logged-in user
                post.save()
                form.save_m2m()  # Save many-to-many fields after saving the instance
                time.sleep(2)
                messages.success(request, 'Post created successfully!')
                return redirect('blogApp:home')
            else:
                # If form is not valid, handle the form data manually
                form_data = {
                    'author': request.user.profile,  # Assign the Profile instance directly
                    'title': request.POST.get('title', ''),
                    'content': request.POST.get('content', '')
                }
                post = Post(author=form_data['author'], title=form_data['title'], content=form_data['content'])
                post.save()
                messages.success(request, 'Post created successfully!')
                time.sleep(2)

                return redirect('blogApp:home')
        else:
            form = PostForm()
        
        return render(request, 'create_post.html', {'form': form})
    else:
        return redirect('blogApp:home')



















# @login_required
def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.user.profile != post.author:
        messages.error(request, 'You are not authorized to update this post.')
        time.sleep(2)

        return redirect('blogApp:post_detail', post_id=post.id)
    
    if request.method == 'POST':

        form = PostForm(request.POST, instance=post)
        if form.is_valid():

            form.save()
            messages.success(request, 'Post updated successfully!')
            return redirect('blogApp:home')

        else:
            print("method reached update")
            post.title = request.POST.get('title', '')
            post.content = request.POST.get('content', '')
            post.save()
            messages.error(request, 'Form is not valid. Please correct the errors.')
            print("heeeeeeeeeeeeeeeeeeeeeeeer")
            return redirect('blogApp:home')
        

    else:
        form = PostForm(instance=post)
    
        return render(request, 'update_post.html', {'form': form, 'post': post})


# @login_required
def delete_post(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        if request.user.profile != post.author:
            messages.error(request, 'You are not authorized to delete this post.')
            
            return redirect('blogApp:home')
        
        if request.method == 'POST':
            print("method reached delete")

            post.delete()
            messages.success(request, 'Post deleted successfully!')
            return redirect('blogApp:home')  # Redirect to home or any other appropriate page after deletion
    
    return render(request, 'delete_post.html', {'post': post})
# @login_required
def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = post.comments.all()
    if request.user.is_authenticated:
        comment_form = CommentForm()
        return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})
    else:
        return render(request, 'post_detail.html',{'post': post, 'comments': comments,})
# @login_required
def create_comment(request, post_id):
    if request.user.is_authenticated:
        post = get_object_or_404(Post, id=post_id)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user.profile
                comment.post = post
                comment.save()
                messages.success(request, 'Comment added successfully!')
                return redirect('blogApp:post_detail',post_id=post_id)
        else:
            form = CommentForm()
    
    return render(request, 'create_comment.html', {'form': form, 'post': post})

def update_comment(request, comment_id):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user.profile != comment.author:
            messages.error(request, 'You are not authorized to update this comment.')
            
            return redirect('blogApp:home', post_id=comment.post.id)
        
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                messages.success(request, 'Comment updated successfully!')
                return redirect('blogApp:post_detail', post_id=comment.post.id)
        else:
            form = CommentForm(instance=comment)
        
    return render(request, 'update_comment.html', {'form': form, 'comment': comment})

# @login_required
def delete_comment(request, comment_id):
    if request.user.is_authenticated :
        comment = get_object_or_404(Comment, id=comment_id)
        if request.user.profile != comment.author:
            messages.error(request, 'You are not authorized to delete this comment.')
            return redirect('blogApp:home')
        
        if request.method == 'POST':
            post_id = comment.post.pk

            comment.delete()
            messages.success(request, 'Comment deleted successfully!')

            return redirect('blogApp:post_detail',post_id=post_id)
        
    return render(request, 'delete_comment.html', {'comment': comment})



class PostListAPIView(ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = CustomPagination

class CategoryListAPIView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CustomPagination

class TagListAPIView(ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    pagination_class = CustomPagination

class CommentListCreateAPIView(ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    pagination_class = CustomPagination
    def get_permissions(self):
        if self.request.method == 'DELETE':
            return [IsOwnerOrReadOnly()]  # Assuming IsOwnerOrReadOnly checks permissions
        return []





class PostRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly]  # Apply custom permission


class CommentDestroyAPIView(generics.DestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def delete(self, request, *args, **kwargs):
        comment = self.get_object()
        if request.user.profile != comment.author:
            return Response({'error': 'You do not have permission to delete this comment.'}, status=status.HTTP_403_FORBIDDEN)
        
        return super().delete(request, *args, **kwargs)