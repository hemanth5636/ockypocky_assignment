from tastypie.constants import ALL
from tastypie.resources import ModelResource
from ..models import Categories


class CategoriesResource(ModelResource):

    class Meta:
        queryset = Categories.objects.all()
        list_allowed_methods = ['get', 'post']
        filtering = {
            'id': ALL,
            'name': ALL,
            'details': ALL,
        }