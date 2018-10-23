from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie.resources import ModelResource
from ..models import SubCategories
from .category_resource import CategoriesResource


class SubCategoryResource(ModelResource):

    category = fields.ForeignKey(CategoriesResource, 'category', full=True)

    class Meta:
        queryset = SubCategories.objects.all()
        list_allowed_methods = ['get', 'post']
        filtering = {
            'category': ALL_WITH_RELATIONS,
            'id': ALL,
            'name': ALL,
            'details': ALL
        }