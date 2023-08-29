from rest_framework.serializers import *
from .models import (
    Client,
    Blog,
    Sponsor,
    Product
)

class ClientSerializer(ModelSerializer):

    class Meta:
        model = Client
        fields = (
            'fullname',
            'phone_number',
        )

class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

class SponsorSerializer(ModelSerializer):

    class Meta:
        model = Sponsor
        fields = '__all__'

class ProductSerializer(ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__' 