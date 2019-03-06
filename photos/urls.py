from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url('^$',views.index,name = 'index'),
    url('^$',views.index,name = 'index'),
    url(r'^search', views.search_image, name='search_image'),
    url(r'^image/(\d+)',views.image,name ='image'),
    url(r'location/(\d+)',views.filter_by_location,name ='location'),
    url(r'category/(\d+)',views.filter_by_category,name ='category'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
