from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework_social_oauth2.authentication import SocialAuthentication
from rest_framework.permissions import AllowAny


@api_view(http_method_names=["GET"])
@authentication_classes(authentication_classes=[SocialAuthentication])
@permission_classes(permission_classes=[AllowAny])
def index(request):
    return Response(data={"app": "sfs-backend"}, status=status.HTTP_200_OK)
