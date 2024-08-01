
from django.urls import path,include
from .import views

urlpatterns = [

    path('',views.index,name='index'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout,name='logout'),
    path('postlist/',views.post_list,name='post_list'),
    path('createPost/',views.create_post,name='create_post'),
    path('updatePost/<int:pk>/',views.update_post,name='update_post'),
    path('deletepost/<int:pk>/',views.delete_post,name='delete_post'),
    path('commentpost/<int:pk>/',views.comment_post,name='comment_post'),
    path('profile/',views.user_profile,name='user_profile')
]