# from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
# from django.contrib.auth import authenticate
# from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView, Request, Response, status
from .models import User
from .serializers import RegisterSerializer
from .permissions import IsUserOwner
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404


class UserView(APIView):
    def get(self, request: Request) -> Response:
        users = User.objects.all()

        serializer = RegisterSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UserDetailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, IsUserOwner]

    def get(self, request, user_id):
        user = get_object_or_404(User, id=user_id)
        self.check_object_permissions(request, user)
        serializer = RegisterSerializer(user)

        return Response(serializer.data)


class LoginView(TokenObtainPairView):
    ...
    # def post(self, request: Request) -> Response:
    #     serializer = LoginSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)

    #     user = authenticate(
    #         username=serializer.validated_data["username"],
    #         password=serializer.validated_data["password"],
    #     )

    #     if not user:
    #         return Response(
    #             {"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN
    #         )

    #     refresh = RefreshToken.for_user(user)

    #     token = {"refresh": str(refresh), "access": str(refresh.access_token)}

    #     return Response(token)


# class LoginView(APIView):
#     def post(self, request: Request) -> Response:
#         serializer = LoginSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         user = authenticate(
#             username=serializer.validated_data["username"],
#             password=serializer.validated_data["password"],
#         )

#         if not user:
#             return Response(
#                 {"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN
#             )

#         return Response({"msg": f"Bem vindo {user.username}"})
