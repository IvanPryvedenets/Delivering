from .models import SelectedProduct


def context_process(request):

    session_key = request.session.session_key

    selectedproducts = SelectedProduct.objects.filter(session=session_key).order_by('id')

    products_count = len(selectedproducts)

    total_price = 0

    for x in selectedproducts:
        total_price += x.total_price

    return {'selectedproducts': selectedproducts, 'products_count': products_count, 'total_price': total_price}

