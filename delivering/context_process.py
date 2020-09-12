from .models import SelectedProduct


def context_process(request):

    selectedproducts = SelectedProduct.objects.order_by('id')

    products_count = len(selectedproducts)

    total_price = 0

    for x in selectedproducts:
        total_price += x.total_price

    return {'selectedproducts': selectedproducts, 'products_count': products_count, 'total_price': total_price}

