from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from noobscribe.auth.serializers import UserSerializer


@api_view(['GET', 'POST'])
def user_detail(request, user_id):
    """
    List all code snippets, or create a new snippet.
    """
    user_model = get_user_model()
    try:
        user = user_model.objects.get(pk=user_id)
    except user_model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    if request.method == 'GET':
        return Response(serializer.data)