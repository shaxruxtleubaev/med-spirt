from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Client,
    Blog,
    Sponsor,
    Product,
)
from .serializers import (
    ClientSerializer,
    BlogSerializer,
    SponsorSerializer,
    ProductSerializer
)

from .telegram_bot import send_data_to_telegram
import asyncio

@api_view(['POST'])
def client_list(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # # Telegram message
            # loop = asyncio.new_event_loop()
            # asyncio.set_event_loop(loop)
            # loop.run_until_complete(send_data_to_telegram(serializer.validated_data))
            # loop.close()

            # Call the asynchronous Telegram messaging function directly
            asyncio.run(send_data_to_telegram(serializer.validated_data))

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['GET'])
def blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        serializer = BlogSerializer(blogs, many=True, context={'request': request})
        return Response(serializer.data)

@api_view(['GET'])
def sponsor_list(request):
    if request.method == 'GET':
        sponsors = Sponsor.objects.all()
        serializer = SponsorSerializer(sponsors, many=True, context={'request': request})
        return Response(serializer.data)

@api_view(['GET'])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True, context={'request': request})
        return Response(serializer.data)