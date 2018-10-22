from tastypie import fields
from tastypie.constants import ALL_WITH_RELATIONS, ALL
from tastypie.resources import ModelResource
from ..models import Products
from inventory.api.sub_category_resource import SubCategoryResource


class ProductResource(ModelResource):

    sub_category = fields.ForeignKey(SubCategoryResource, 'sub_category', full=True)

    class Meta:
        queryset = Products.objects.all()
        allowed_methods = ['get', 'post']
        resource_name = 'products'
        filtering = {
            'sub_category': ALL_WITH_RELATIONS,
            'id': ALL,
            'name': ALL,
            'details': ALL
        }