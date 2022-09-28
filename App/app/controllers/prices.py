from app import app
from app.service import aliexpress, amazon, americanas, bling, kabum, magazineluiza, mercadolivre, olist, pontofrio, shopee, submarino
from flask import Flask, redirect, url_for, request, jsonify, render_template


@app.route('/prices/<sku>/<goverment_taxes>/<price>')
def prices(sku, goverment_taxes, price):

    sku = "3920RW"

    price = float(price)

    produto = bling.getProductInfo(sku)

    mercadolivre_result = mercadolivre.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    amazon_result = amazon.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    americanas_result = americanas.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    pontofrio_result = pontofrio.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    kabum_result = kabum.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    magazineluiza_result = magazineluiza.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    shopee_result = shopee.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    aliexpress_result = aliexpress.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    submarino_result = submarino.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    olist_result = olist.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    # End_Submarino=============================================================

    prices_result = [
        {"service": "mercadoLivre",
         "tax": "14% + R$ 5,00",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(mercadolivre_result, 2)},
        {"service": "amazon",
         "tax": "15",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(amazon_result, 2)},
        {"service": "americanas",
         "tax": f"{round(americanas_result.tax, 0)}%",
         "shipping": americanas_result.shipping,
         "goverment_taxes": americanas_result.governement_taxes,
         "amount": round(americanas_result.selling_price, 2)},
        {"service": "pontofrio",
         "tax": "18",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(pontofrio_result, 2)},
        {"service": "kabum",
         "tax": "14",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(kabum_result, 2)},
        {"service": "magazine",
         "tax": "20",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(magazineluiza_result, 2)},
        {"service": "shopee",
         "tax": f"{round(shopee_result.tax, 0)}%",
         "shipping": shopee_result.shipping,
         "goverment_taxes": shopee_result.governement_taxes,
         "amount": round(shopee_result.selling_price, 2)},
        {"service": "aliexpress",
         "tax": "10",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(aliexpress_result, 2)},
        {"service": "submarino",
         "tax": f"{round(submarino_result.tax, 0)}%",
         "shipping": submarino_result.shipping,
         "goverment_taxes": submarino_result.governement_taxes,
         "amount": round(submarino_result.selling_price, 2)},
        {"service": "olist",
         "tax": "21",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(olist_result, 2)}
    ]

    # json.dumps(prices_result)

    return jsonify(prices_result)
