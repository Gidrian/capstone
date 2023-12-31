# restaurant/urls.py
from django.urls import path, include

from . import views

from rest_framework.routers import DefaultRouter

router: DefaultRouter = DefaultRouter()
router.register(r'tables', views.BookingViewSet)

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name="about"),
    path('menu/', views.menu, name='menu'),
    path('booking/', include(router.urls)),
    
]
