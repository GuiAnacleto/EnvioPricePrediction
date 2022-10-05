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
    payload = {'price': price, 'category_id': product_category}
    price_response = requests.get(url, params=payload)
    product_fee_json = json.dumps(price_response.json()[0])
    product_fee_str = json.loads(product_fee_json)
    product_fee = product_fee_str['sale_fee_amount']

    print(f"fee: {product_fee}")

    product_weight = float(product.pesoBruto)

    if product_weight <= 500:
        shipping_result = 25.42
    if product_weight > 500 and product_weight <= 1000:
        shipping_result = 27.67
    if product_weight > 1000 and product_weight <= 2000:
        shipping_result = 28.42
    if product_weight > 2000 and product_weight <= 5000:
        shipping_result = 35.17
    if product_weight > 5000 and product_weight <= 9000:
        shipping_result = 52.42
    if product_weight > 9000 and product_weight <= 13000:
        shipping_result = 82.42

    governement_taxes_result = price * governement_taxes
    if price < 79:
        price_result = price - product_fee - \
            shipping_result - governement_taxes_result - 5
    else:
        price_result = price - product_fee - shipping_result - governement_taxes_result

    return product_price(price=price, tax=product_fee, shipping=shipping_result, governement_taxes=governement_taxes_result, selling_price=price_result)
