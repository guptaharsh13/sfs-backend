from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(http_method_names=("GET",))
def index(request):
    return Response(data={"app": "sfs-backend"}, status=status.HTTP_200_OK)
