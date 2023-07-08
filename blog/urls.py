from django.urls import path, re_path

from .views import(
    blog_post_list_view,
    blog_post_detail_view,
    blog_post_delete_view,
    blog_post_update_view
)

urlpatterns = [
    path('', blog_post_list_view), #this one works for blogs -> list of blogs
    path('<str:slugme>/', blog_post_detail_view),
    path('<str:slugme>/delete/', blog_post_delete_view),
    path('<str:slugme>/edit/', blog_post_update_view)
]
