from django.shortcuts import render
from .models import Product 
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.contrib.auth.models import User
# Create your views here.

class ProductAPI(APIView):

    @swagger_auto_schema(
            Response={200:"List of the Product"}
    )
    def get(self , request):
        product = Product.objects.all().values("name","description","quantity","price","author")
        return Response(list(product), status= status.HTTP_200_OK)
    


    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="Product name"),
                "quantity": openapi.Schema(type=openapi.TYPE_INTEGER, description="Initial quantity"),
                "price": openapi.Schema(type=openapi.TYPE_NUMBER, format="float", description="Product price"),
                "description": openapi.Schema(type=openapi.TYPE_STRING, format="String", description="this is a nice product long lasting"),
                
            },
            required=["name", "quantity", "price"],
        ),
        responses={201: "Product created successfully"}
    )


    def post(self , request):
        name = request.data.get("name")
        description = request.data.get("description")
        price = request.data.get("price")
        quantity= request.data.get("quantity")

        product = Product.objects.create(
            name=name,
            description=description,
            price=price,
            quantity=quantity
        )
        return Response(
            "successfully created",status=status.HTTP_201_CREATED
        )
        

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
                "quantity": openapi.Schema(type=openapi.TYPE_INTEGER),
                "price": openapi.Schema(type=openapi.TYPE_NUMBER, format="float"),
                "description": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: "Updated", 404: "Not found"}
    )

    def put(self, request):

        product_name = request.data.get("name")
        P_quantity = request.data.get("quantity")
        P_price = request.data.get("price")
        P_desription= request.data.get("description")

        try:

            product = Product.objects.get(name=product_name) 
            product.quantity=P_quantity
            product.price=P_price
            product.description=P_desription

            product.save()

            return Response("Product Updated",status= status.HTTP_201_CREATED)
            
        except Product.DoesNotExist:

            return Response({"error:","Product not found"},status= status.HTTP_404_NOT_FOUND)

    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "name": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: "deleted", 404: "Not found"}
    )

    def delete(self, request):
        username=request.data.get("name")

        try:
            print(username)
            product = Product.objects.get(name=username)
            product.delete()
            return Response("Product deleted successfully", status= status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response("Product not found ", status= status.HTTP_404_NOT_FOUND)
        


class PurchaseProduct(APIView):


    @swagger_auto_schema(
        request_body=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "product_name": openapi.Schema(type=openapi.TYPE_STRING),
                "user_name": openapi.Schema(type=openapi.TYPE_STRING),
            },
        ),
        responses={200: "product purchessed !!! mazee karooo ", 406: "Not found"}
    )

    def put(self , request):

        prod_name = request.data.get("product_name")
        user_name = request.data.get("user_name")

        try:
            product = Product.objects.get(name=prod_name)
            user = User.objects.get(username=user_name)

            if product.quantity > 0 and product and user :
                if user_name not in product.author:
                    product.author.append(user_name)
                product.quantity-=1
                product.save()
                return Response("product added to cart yeahhhh!!!!", status= status.HTTP_202_ACCEPTED)
        except Exception as e:
            return Response(f"Error is {e}" , status= status.HTTP_406_NOT_ACCEPTABLE)




















