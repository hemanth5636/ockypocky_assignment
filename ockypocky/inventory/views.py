from django.http import HttpResponse
from django.template.loader import get_template
from inventory import utils


def displayProductsData(request):

    products = utils.getProductsData()
    template = get_template('tables.html')
    response = template.render({'products':products})
    return HttpResponse(response)