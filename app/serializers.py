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
        fields = '__all__'

class BlogSerializer(ModelSerializer):

    class Meta:
        model = Blog
        fields = '__all__'

class SponsorSerializer(ModelSerializer):

    image_url = SerializerMethodField()

    class Meta:
        model = Sponsor
        fields = '__all__'

    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
        return None

class ProductSerializer(ModelSerializer):

    image_url = SerializerMethodField()

    class Meta:
        model = Product
        fields = '__all__' 
    
    def get_image_url(self, obj):
        request = self.context.get('request')
        if obj.image:
            image_url = obj.image.url
            return request.build_absolute_uri(image_url)
        return None
    