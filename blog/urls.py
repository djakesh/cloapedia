from django.urls import path
from .views import (
    main_page, create_post, my_posts, category_posts,
    search, post_detail, post_update, post_delete, rate_post)

urlpatterns = [
    path('rate/<int:pk>', rate_post, name='rate'),
    path('post_delete/<int:pk>/', post_delete, name='post_delete'),
    path('post_update/<int:pk>/',post_update, name='post_update'),
    path('post_detail/<int:pk>/', post_detail, name='post_detail'),
    path('category/<int:pk>/', category_posts, name='category_details'),
    path('my-posts/', my_posts, name='my_posts'),
    path('create-post/', create_post, name='post_create'),
    path('search/', search, name='search'),
    path('', main_page, name='main_page'),
]
