"""
URL configuration for bicicletas project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path,include
from categoryapp.routers import (router_Category)
from productapp.routers import router_Product
from productxstoreapp.routers import router_Productxstore
from storeapp.routers import router_store




urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/Category/', include(router_Category.urls)),
    path('api/Product/', include(router_Product.urls)),
    path('api/productxstore/', include(router_Productxstore.urls)),
    path('api/store/', include(router_store.urls)),
]
