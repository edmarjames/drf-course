"""drf_course URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from django.contrib import admin
# import views defined in the core module
from core import views as core_views
# import views defined in the ecommerce module
from ecommerce import views as ecommerce_views
# import DefaultRouter from the Django Rest Framework.
from rest_framework import routers
# import obtain_auth_token from rest_framework
from rest_framework.authtoken.views import obtain_auth_token

# A new instance of the DefaultRouter is created using router = routers.DefaultRouter(). This is a convenience class that automatically generates the URL patterns for the API views registered with it.
router = routers.DefaultRouter()
router.register(r'item', ecommerce_views.ItemViewSet, basename='item')
router.register(r'order', ecommerce_views.OrderViewSet, basename='order')

# The urlpatterns list is then defined using the router's generated URL patterns
urlpatterns = router.urls

# Two additional URL patterns are added to the urlpatterns
urlpatterns += [
    path('admin/', admin.site.urls),
    # ContactAPIView class view defined in the core module.
    path('contact/', core_views.ContactAPIView.as_view()),
    path('api-token-auth/', obtain_auth_token), #gives us access to token auth
]

# The router.urls generated by DefaultRouter maps URLs for the registered API views, while the path() function is used to map custom URL paths to other views or pages.