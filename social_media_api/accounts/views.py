from django.shortcuts import render, get_object_or_404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from django.contrib.auth import login
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import CustomUser
from .serializers import UserSerializer, RegistrationSerializser, LoginSerializer


# Create your views here.
class RegisterView(generics.CreateAPIView):
    serializer_class = RegistrationSerializser
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        return Response({
            'user': UserSerializer(user).data,
            'token': user.token
        }, status=status.HTTP_201_CREATED)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, *args, **kwargs):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        token, created = Token.objects.get_or_create(user=user)
        login(request, user)
        return Response({
            'user': UserSerializer(user).data,
            'token': token.key
        })

class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user
    
class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(CustomUser, pk=user_id)

        # Prevent following self
        if target.pk == request.user.pk:
            return Response(
                {"detail": "You cannot follow yourself"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        if request.user.is_following(target):
            return Response(
                {
                    "detail": "Already following.",
                    "me": UserSerializer(request.user, context={"request": request}).data
            },
            status=status.HTTP_200_OK
            )
        
        request.user.follow(target)
        return Response(
            {
                "detail": "You are now following this user",
                "me": UserSerializer(request.user, context={"request": request}).data
            },
            status=status.HTTP_201_CREATED
        )

class UnfollowUserView(generics.GenericAPIView):
    """
    POST /auth/unfollow/<user_id>/
    """
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id, *args, **kwargs):
        target = get_object_or_404(CustomUser, pk=user_id)

        if target.pk == request.user.pk:
            return Response(
                {"detail": "You cannot unfollow yourself."},
                status=status.HTTP_400_BAD_REQUEST
            )

        if not request.user.is_following(target):
            # Not following → idempotent success
            return Response(
                {
                    "detail": "You were not following.",
                    "me": UserSerializer(request.user, context={"request": request}).data
                },
                status=status.HTTP_200_OK
            )

        request.user.unfollow(target)
        return Response(status=status.HTTP_204_NO_CONTENT)

