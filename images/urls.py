from  django.urls import include, path
# from .views import get_images, get_image, get_image_200, get_images_400
from .views import ImageView, LinkView


urlpatterns = [
    path("images", ImageView.as_view()),
    path("links", LinkView.as_view())
    # path("api/original/<int:id>", get_image),
  
    # path("api/200/<int:id>", get_image_200),
    # path("api/400/<int:id>", get_images_400)
] 