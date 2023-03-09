from django.utils import timezone
from PIL import Image as _Image
from rest_framework import serializers
from typing import Tuple
from .models import Image, Link



def new_filename(filename :str, size :int) -> str:
    '''generates new name for a resized image'''
    name = str(filename).rsplit(".")[0]
    ext = str(filename).rsplit(".")[1]
    new_name = f"{name}-{size}.{ext}"
    return new_name

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id','user','name', 'image']

class BasicSerializer(ImageSerializer):
    image200 = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ['id','user','name', 'image','image200']
    
    def get_image200(self, data):
        SIZE = 200
        if data.image:
            image = _Image.open(f"{data.image}")
            new_name = new_filename(f"{data.image}", SIZE)
            image.thumbnail((4*SIZE, SIZE))
            image.save(new_name)  
            new_name = new_filename(data.image,SIZE)
            image_path = f'{new_name}'
            return '/'+image_path
        else:
            return None

class PremiumSerializer(BasicSerializer):
    image400 = serializers.SerializerMethodField()
    class Meta:
        model = Image
        fields = ['id','user','name','image','image200','image400']
    
    def get_image400(self, data):
        SIZE = 400
        if data.image:
            image = _Image.open(f"{data.image}")
            new_name = new_filename(f"{data.image}", SIZE)
            image.thumbnail((4*SIZE, SIZE))
            image.save(new_name)  
            new_name = new_filename(data.image,SIZE)
            image_path = f'{new_name}'
            return '/'+image_path
        else:
            return None
        
class EnterpriseSerializer(PremiumSerializer):
    class Meta:
        model = Image
        fields = ['id','user','name','image','image200','image400']

class LinkSerializer(serializers.ModelSerializer):
    url = serializers.SerializerMethodField()
    expires_at = serializers.SerializerMethodField()
    class Meta:
        model = Link
        fields = ['img', 'expiration_time', 'url', 'expires_at']
    
    def get_url(self,data):
        image = Image.objects.get(pk=data.img)
        print(data.img)
        print (image)
        url = str(image.image)
        print(url)
        return '/'+url
    
    def get_expires_at(self,data):
        return (timezone.now() + timezone.timedelta(
            seconds=data.expiration_time
            )).strftime("%m.%d.%Y, %H:%M:%S")