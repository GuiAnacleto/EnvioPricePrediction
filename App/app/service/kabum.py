from app import app
from app.models import product_price
# https://plugg.to/kabum-como-vender-no-marketplace-guia-atualizado-para-vendedores/


def getProductPrice(price, governement_taxes):
    tax_result = price * 0.14
    shipping_result = price * 0
    governement_taxes_result = price * governement_taxes

    price_result = price - tax_result - shipping_result - governement_taxes_result

    return product_price(price=price, tax=tax_result, shipping=shipping_result, governement_taxes=governement_taxes_result, selling_price=price_result)
