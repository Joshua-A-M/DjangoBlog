from django.shortcuts import get_object_or_404, render
from .models import Post
from django.http import Http404

# Create your views here.

#   takes the equest object as the only parameter
#   parameter is required by all views
#   retrieves all the posts with the PUBLISHED status using the published manager
def post_list(request):
    posts = Post.published.all()

    #   use the render() shortcut to render the list of posts with the given templates
    return render(
        request,
        'blog/post/list.html',
        {'posts': posts}
    )

#   Tekes the id argument of a post and renders the Post object with the given id by calling the get() method on the
#   published manager
# def post_detail(request, id):
#     try:
#         post = Post.published.get(id=id)
#
#     except Post.DoesNotExist:
#         #   Raise the Http404 exception to return an HTTP 404 error if the model DoesNotExist exception is raised
#         raise Http404('No Post found.')
#     return render(
#         request,
#         'blog/post/detail.html',
#         {'post' : post}
#     )


def post_detail(request, id):
    #   Use the get_object_or_404() shortcut to retrieve the desired post.
    #   Retrieves the object that matches the given parameters or an HTTP 404 exception if no object is found
    post = get_object_or_404(
        Post,
        id=id,
        satus=Post.Status.PUBLISHED
    )
    return render(
        request,
        'blog/post/detail.html',
        {'post': post}
    )





