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
import requests
from src.settings.base import (
    TELEGRAM_CHAT_ID,
    TELEGRAM_BOT_TOKEN
)

@api_view(['POST'])
def client_list(request):
    if request.method == 'POST':
        serializer = ClientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            # Telegram info
            chat_id = TELEGRAM_CHAT_ID  
            message_text = f'Новый клиент: \
                \n\nКлиент: {serializer.instance.fullname} \
                \nТелефон номер: {serializer.instance.phone_number} \
                \n\nfarrux-begzod.uz'
            bot_token = TELEGRAM_BOT_TOKEN  

            url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
            payload = {
                'chat_id': chat_id,
                'text': message_text,
            }

            response = requests.post(url, data=payload)

            if response.status_code == 200:
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            else:
                return Response(
                    {"error": "Failed to send Telegram message"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
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