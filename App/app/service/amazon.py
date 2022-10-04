from app import app
from app.models import product_price
# https://venda.amazon.com.br/precos
# https://developer-docs.amazon.com/sp-api/
# https://developer-docs.amazon.com/sp-api/docs/product-fees-api-v0-reference


def getProductPrice(price, governement_taxes):

    tax_result = price * 0.16
    shipping_result = price * 0.06
    governement_taxes_result = price * governement_taxes
    price_result = price - tax_result - shipping_result - governement_taxes_result

    return product_price(price=price, tax=tax_result, shipping=shipping_result, governement_taxes=governement_taxes_result, selling_price=price_result)
