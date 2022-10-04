from app import app
from app.models import product_price
# https://desenvolvedores.skyhub.com.br/
# Plataforma SkyHub: http://in.skyhub.com.br/users/sign_in#/
#Usuário: corporativo@e-nvio.com
# Senha: 1yXcnh8fwsk=


def getProductPrice(price, governement_taxes):

    tax_result = price * 0.16
    fix_tax = 5
    shipping_result = price * 0.06
    governement_taxes_result = price * governement_taxes

    if price < 40:
        price_result = price - tax_result - shipping_result - governement_taxes_result
    if price >= 40:
        price_result = price - fix_tax - tax_result - \
            shipping_result - governement_taxes_result

    return product_price(price=price, tax=tax_result, shipping=shipping_result, governement_taxes=governement_taxes_result, selling_price=price_result)
