from app import app
from app.service import aliexpress, amazon, americanas, bling, kabum, magazineluiza, mercadolivre, olist, pontofrio, shopee, submarino
from flask import Flask, redirect, url_for, request, jsonify, render_template


@app.route('/prices/<sku>/<goverment_taxes>/<price>', methods=['GET'])
def prices(sku, goverment_taxes, price):

    sku = "3920RW"
    goverment_taxes = float(goverment_taxes)/100
    price = float(price)

    #produto = bling.getProductInfo(sku)

    mercadolivre_result = mercadolivre.getProductPrice(
        sku=sku, price=price, governement_taxes=goverment_taxes)

    amazon_result = amazon.getProductPrice(
        price=price, governement_taxes=goverment_taxes)

    americanas_result = americanas.getProductPrice(
        price=price, governement_taxes=goverment_taxes)

    pontofrio_result = pontofrio.getProductPrice(
        price=price, governement_taxes=goverment_taxes)

    kabum_result = kabum.getProductPrice(
        price=price, governement_taxes=goverment_taxes)

    magazineluiza_result = magazineluiza.getProductPrice(
        price=price, governement_taxes=goverment_taxes)

    shopee_result = shopee.getProductPrice(
        price=price, governement_taxes=goverment_taxes)

    aliexpress_result = aliexpress.getProductPrice(
        price=price, governement_taxes=goverment_taxes)

    submarino_result = submarino.getProductPrice(
        price=price, governement_taxes=goverment_taxes)

    olist_result = olist.getProductPrice(
        price=price, governement_taxes=float(goverment_taxes)/100)

    # End_Submarino=============================================================

    prices_result = [
        {"service": "mercadoLivre",
         "tax": f"{mercadolivre_result.tax}",
         "shipping": mercadolivre_result.shipping,
         "goverment_taxes": mercadolivre_result.governement_taxes,
         "amount": mercadolivre_result.selling_price},
        {"service": "amazon",
         "tax": f"{round(amazon_result.tax, 0)}%",
         "shipping": amazon_result.shipping,
         "goverment_taxes": amazon_result.governement_taxes,
         "amount": round(amazon_result.selling_price, 2)},
        {"service": "americanas",
         "tax": f"{round(americanas_result.tax, 0)}%",
         "shipping": americanas_result.shipping,
         "goverment_taxes": americanas_result.governement_taxes,
         "amount": round(americanas_result.selling_price, 2)},
        {"service": "pontofrio",
         "tax": f"{round(pontofrio_result.tax, 0)}%",
         "shipping": pontofrio_result.shipping,
         "goverment_taxes": pontofrio_result.governement_taxes,
         "amount": round(pontofrio_result.selling_price, 2)},
        {"service": "kabum",
         "tax": f"{round(kabum_result.tax, 0)}%",
         "shipping": kabum_result.shipping,
         "goverment_taxes": kabum_result.governement_taxes,
         "amount": round(kabum_result.selling_price, 2)},
        {"service": "magazine",
         "tax": f"{round(magazineluiza_result.tax, 0)}%",
         "shipping": magazineluiza_result.shipping,
         "goverment_taxes": magazineluiza_result.governement_taxes,
         "amount": round(magazineluiza_result.selling_price, 2)},
        {"service": "shopee",
         "tax": f"{shopee_result.tax}",
         "shipping": shopee_result.shipping,
         "goverment_taxes": shopee_result.governement_taxes,
         "amount": shopee_result.selling_price},
        {"service": "aliexpress",
         "tax": f"{round(aliexpress_result.tax, 0)}%",
         "shipping": aliexpress_result.shipping,
         "goverment_taxes": aliexpress_result.governement_taxes,
         "amount": round(aliexpress_result.selling_price, 2)},
        {"service": "submarino",
         "tax": f"{round(submarino_result.tax, 0)}%",
         "shipping": submarino_result.shipping,
         "goverment_taxes": submarino_result.governement_taxes,
         "amount": round(submarino_result.selling_price, 2)},
        {"service": "olist",
         "tax": f"{round(olist_result.tax, 0)}%",
         "shipping": olist_result.shipping,
         "goverment_taxes": olist_result.governement_taxes,
         "amount": round(olist_result.selling_price, 2)},
    ]

    # json.dumps(prices_result)

    return jsonify(prices_result)
