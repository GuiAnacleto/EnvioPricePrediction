from app import app
from app.models import product_price


def getProductPrice(price, governement_taxes):

    tax_result = price * 0.16
    fix_tax = 5
    shipping_result = price * 0.06
    governement_taxes_result = price * governement_taxes

    price_result = price - fix_tax - tax_result - \
        shipping_result - governement_taxes_result

    return product_price(price=price, tax=tax_result, shipping=shipping_result, governement_taxes=governement_taxes_result, selling_price=price_result)
