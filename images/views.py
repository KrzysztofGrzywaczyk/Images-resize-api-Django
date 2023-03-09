from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from typing import Tuple
from .models import Image, Link
from .serializer import BasicSerializer, EnterpriseSerializer, ImageSerializer, LinkSerializer, PremiumSerializer


def resize(new_height :int,height :int,width :int) -> Tuple[int,int]: 
    width=int(width//(height/new_height))
    return (new_height, width)

def new_filename(filename :str, size :int) -> str:
    name = str(filename).rsplit(".")[0]
    ext = str(filename).rsplit(".")[1]
    new_name = f"{name}-{size}.{ext}"
    return new_name

def is_member(user, group_name):
    """Check if user is a mamper of a group of <group_name>"""
    return user.groups.filter(name=f'{group_name}').exists()

def get_serializer_class(self, request):
        if is_member(request.user, group_name='Enterprise'):
            return EnterpriseSerializer
        elif is_member(request.user, group_name='Premium'):
            return PremiumSerializer
        else:
            return BasicSerializer 


class ImageView(APIView):     
    def get(self, request):
        images = Image.objects.all().filter(user=request.user)
        user = request.user
        if not user.is_authenticated:   #intentional doubling with query - improve safety 
            images = Image.objects.none()
        serializer = get_serializer_class(self, request)(images, many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = get_serializer_class(self, request)(data = request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            data = serializer.data
            if get_serializer_class(self, request) == BasicSerializer:
                del data['image']
            return Response(data,status=status.HTTP_201_CREATED)
        

class LinkView(APIView):
    def post(self,request):
        serializer = LinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=self.request.user)
            return Response(serializer.data,status=status.HTTP_201_CREATED)
