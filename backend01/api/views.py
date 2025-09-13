from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi


class createAPI(APIView):

    def get(self, request):
        users = User.objects.all().values("id", "username", "email")  # no serializer
        return Response(list(users), status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING, description="Unique username"),
                "password": openapi.Schema(type=openapi.TYPE_STRING, description="Password for the user"),
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="Email address"),
            },
            required=["username", "password"],
        ),
        responses={201: "User created successfully"}
    )
    def post(self, request):
        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "User already exists"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, password=password, email=email)
        return Response(
            {"id": user.id, "username": user.username, "email": user.email},
            status=status.HTTP_201_CREATED
        )

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING, description="Username to search"),
                "email": openapi.Schema(type=openapi.TYPE_STRING, description="New email to update"),
            },
            required=["username", "email"],
        ),
        responses={200: "User email updated successfully", 404: "User not found"}
    )
    def put(self, request):
        username = request.data.get("username")
        email = request.data.get("email")

        if not username or not email:
            return Response({"error": "username and email are required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

        user.email = email
        user.save()

        return Response({"id": user.id, "username": user.username, "email": user.email}, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "username": openapi.Schema(type=openapi.TYPE_STRING, description="Username to search"),
            },
            required=["username"],
        ),
        responses={200: "User deleted successfully", 404: "User not found"}
    )
    def delete(self, request):
        username = request.data.get("username")

        try:
            user = User.objects.get(username=username)
            user.delete()
            return Response({"message": "User deleted successfully"}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
        