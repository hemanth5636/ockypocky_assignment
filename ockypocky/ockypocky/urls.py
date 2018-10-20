"""ockypocky URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from tastypie.api import Api
from inventory.api.category_resource import CategoriesResource
from inventory.api.sub_category_resource import SubCategoryResource
from inventory.api.products_resource import ProductResource

api = Api(api_name='v1')
api.register(CategoriesResource())
api.register(SubCategoryResource())
api.register(ProductResource())

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(api.urls))
]
