from django.contrib import admin
from django.urls import path,include,re_path
from django.conf import settings

from django.views.static import serve
from .views import (home,create_post,update_post,delete_post,post_detail,create_comment,update_comment,delete_comment,
PostListAPIView,PostRetrieveUpdateDestroyAPIView,CategoryListAPIView,TagListAPIView,CommentListCreateAPIView,CommentDestroyAPIView)
app_name = "blogApp"
urlpatterns = [

path("",home,name="home"),
    
    # Post URLs
    path('post/create/', create_post, name='create_post'),
    path('post/<int:post_id>/update/', update_post, name='update_post'),
    path('post/<int:post_id>/delete/', delete_post, name='delete_post'),
    path('post/<int:post_id>/', post_detail, name='post_detail'),
    path('post/<int:post_id>/comment/create/', create_comment, name='create_comment'),
   
    # Comment URLs
    path('comment/<int:comment_id>/update/', update_comment, name='update_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
    # API Is THE Following 

    path('api/comments/<int:pk>/', CommentDestroyAPIView.as_view(), name='comment-detail'),
    path('api/comments/', CommentListCreateAPIView.as_view(), name='comment-list-create'),

    path('api/posts/<int:pk>/', PostRetrieveUpdateDestroyAPIView.as_view(), name='post-detail'),
    path('api/posts/', PostListAPIView.as_view(), name='post-list-create'),
    path('api/categories/', CategoryListAPIView.as_view(), name='category-list'),
    path('api/tags/', TagListAPIView.as_view(), name='tag-list'),

]

from django.urls import path
from .views import (
    home, create_post, update_post, delete_post, post_detail,
    create_comment, update_comment, delete_comment,
    PostListAPIView, PostRetrieveUpdateDestroyAPIView,
    CategoryListAPIView, TagListAPIView, CommentListCreateAPIView, CommentDestroyAPIView
)
