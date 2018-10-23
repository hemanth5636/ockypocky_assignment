import urllib.request
import json
from inventory.models import Products

def getProductsData():

    productsData = Products.objects.all()
    products = []
    for productData in productsData:
        product = {}
        product['name'] = productData.name
        product['details'] = productData.details
        product['sub_category'] = productData.sub_category.name
        product['category'] = productData.sub_category.category.name

        products.append(product)
        print(product)
    return products