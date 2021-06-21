from django.urls import path
from .views import products

app_name = 'mainapp'

# urlpatterns = [
#     path('', products, name='index'),
#     path('product/<int:pk>/', products, name='products'),
# ]


urlpatterns = [
    path('', products, name='index'),
    path('category/<int:pk>/', products, name='category'),
    path('category/<int:pk>/page/<int:page>/', products, name='page'),
    path('product/<int:pk>/', products, name='products'),
]