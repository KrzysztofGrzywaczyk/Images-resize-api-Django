import factory
from images.models import Image, Link


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image
    name = ('test_name')


class LinkFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Link
    img = 2
    expiration_time = 30