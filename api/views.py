from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import User,Profile
from .serializers import ProfileSerializer,UserSerializer,MyTokenObtainPairSerializer

#User register
@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(
            {"message" : "User create successfully"},
            status=status.HTTP_201_CREATED
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#login by class
class MyLoginView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

#user list
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_list(request):
    users = User.objects.all().order_by('-id')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

