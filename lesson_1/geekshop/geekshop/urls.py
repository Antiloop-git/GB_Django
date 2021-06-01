from django.contrib import admin
from django.urls import path, include
from mainapp import urls
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', include(urls, namespace='products'), name='products'),
    path('', views.index, name='index'),
    path('', views.index, name='products_all'),
    path('', views.index, name='products_home'),
    path('contact/', views.contact, name='contact'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)