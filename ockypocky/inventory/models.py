from django.db import models


# Create your models here.
class Categories(models.Model):

    name = models.CharField(max_length=50,  null=False)
    details = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = 'categories'


class SubCategories(models.Model):

    category = models.ForeignKey(Categories, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False)
    details = models.CharField(max_length=100, null=False)

    class Meta:
        db_table = "subcategory"


class Products(models.Model):

    sub_category = models.ForeignKey(SubCategories, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=False)
    details = models.CharField(max_length=150, null=False)

    class Meta:
        db_table = "products"



