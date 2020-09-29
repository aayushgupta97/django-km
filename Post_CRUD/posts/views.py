from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Post


def get_dict_from_post(post_obj):
    post_dict = {}
    if post_obj:
        post_dict["id"] = post_obj.id
        post_dict["title"] = post_obj.title
        post_dict["message"] = post_obj.message
    return post_dict


def make_response(item):
    return Response({
        "Response": item
    })


class PostViewer(APIView):
    def get(self, request):
        response = []
        all_posts = Post.objects.all()
        for post in all_posts:
            response.append(get_dict_from_post(post))
        return make_response(response)

    def post(self, request):
        title = request.data.get("title")
        message = request.data.get("message")
        if not title:
            return make_response("Title Missing")
        if not message:
            return make_response("Message Missing")

        new_post = Post()
        new_post.title = title
        new_post.message = message

        new_post.save()
        return make_response({"id": new_post.id})


class PostManager(APIView):
    def get(self, request, post_id):
        response = "No Post Found"
        try:
            current_post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            current_post = None

        if current_post:
            response = get_dict_from_post(current_post)
        return make_response(response)

    def put(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return make_response("No Post Found")

        new_title = request.data.get("title")
        new_message = request.data.get("message")
        if new_title:
            post.title = new_title
        if new_message:
            post.message = new_message

        post.save()
        return make_response("Post updated successfully")

    def delete(self, request, post_id):
        try:
            post = Post.objects.get(id=post_id)
        except Post.DoesNotExist:
            return make_response("No Post Found")

        post.delete()
        return make_response("Post Deleted Successfully")
