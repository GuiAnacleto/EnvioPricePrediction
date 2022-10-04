import requests
import json
import sys
from .bling import getProductInfo
from app.models import product_price
from app import app
# postman
# login: edupfranco@gmail.com
# senha: #b0^z5NSeGc6
# TG-633c6af9b60a880001ae55d6-391607939

# bearer: APP_USR-1260458013278330-100413-21d254d212fbb297640167fd9e87e66d-391607939
# https://developers.mercadolivre.com.br/pt_br/calcular-o-custo-frete-e-o-handling-time


def getProductPrice(sku, price, governement_taxes):

    product = getProductInfo(sku)

    url = 'https://api.mercadolibre.com/sites/MLA/domain_discovery/search'
    auth_token = 'APP_USR-1260458013278330-100413-21d254d212fbb297640167fd9e87e66d-391607939'
    hed = {'Authorization': 'Bearer ' + auth_token}
    payload = {'limit': '1', 'q': product.name}

    category_response = requests.get(url, params=payload, headers=hed)
    product_json = json.dumps(category_response.json()[0])
    product_str = json.loads(product_json)
    product_category = product_str['category_id']

    url = 'https://api.mercadolibre.com/sites/MLB/listing_prices'
    auth_token = 'APP_USR-1260458013278330-100413-21d254d212fbb297640167fd9e87e66d-391607939'
    hed = {'Authorization': 'Bearer ' + auth_token}
    payload = {'price': price, 'category_id': product_category}

    price_response = requests.get(url, params=payload, headers=hed)
    product_fee_json = json.dumps(price_response.json()[0])
    product_fee_str = json.loads(product_fee_json)
    product_fee = product_fee_str['sale_fee_amount']

    product_fee = float(product_fee)
    product_fee = product_fee/100

    tax_result = price * product_fee
    shipping_result = price * 0.06
    governement_taxes_result = price * governement_taxes
    price_result = price - tax_result - shipping_result - governement_taxes_result

    return product_price(price=price, tax=tax_result, shipping=shipping_result, governement_taxes=governement_taxes_result, selling_price=price_result)
