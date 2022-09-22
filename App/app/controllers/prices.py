from app import app
from app.service import bling, shopee, americanas, submarino
from flask import Flask, redirect, url_for, request, jsonify, render_template

@app.route('/prices/<sku>/<goverment_taxes>/<price>')
def prices(sku, goverment_taxes, price):
    
    sku = "3920RW"    

    price = float(price)    

    produto = bling.getProductInfo(sku)

    #MercadoLivre=================================================================

    if price < 79: ml_price = price * 1.14 + 5 
    else: ml_price = price * 1.14

    #End_MercadoLivre=============================================================

    #Amazon=================================================================
    
    if price * 1.15 < 1: amazon_price = price + 1
    else: amazon_price = price * 1.15

    #End_Amazon=============================================================

    #Americanas=================================================================
    
    americanas_result = americanas.getProductPrice(price=price, governement_taxes=float(goverment_taxes)/100)

    #End_Americanas=============================================================

    #PontoFrio=================================================================
    
    ponto_result = price * 1.18

    #End_PontoFrio=============================================================

    #Kabum=================================================================
    
    kabum_result = price * 1.14

    #End_Kabum=============================================================

    #Magazine=================================================================
    
    magazine_result = price * 1.20

    #End_Magazine=============================================================

    #Shopee=================================================================
    
    shopee_result = shopee.getProductPrice(price=price, governement_taxes=float(goverment_taxes)/100)

    #End_Shopee=============================================================

    #Shopee=================================================================
    
    aliexpress_result = price * 1.10

    #End_Shopee=============================================================

    #Submarino=================================================================

    submarino_result = submarino.getProductPrice(price=price, governement_taxes=float(goverment_taxes)/100)

    #End_Submarino=============================================================

    #Submarino=================================================================
    
    olist_result = price * 1.21 + 5

    #End_Submarino=============================================================

    prices_result = [
        {"service":"mercadoLivre",
         "tax": "14% + R$ 5,00",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount":round(ml_price, 2)},
        {"service":"amazon",
         "tax": "15",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(amazon_price, 2)},
        {"service":"americanas",
         "tax": f"{round(americanas_result.tax, 0)}%",
         "shipping": americanas_result.shipping,
         "goverment_taxes": americanas_result.governement_taxes,
         "amount": round(americanas_result.selling_price, 2)},
        {"service":"pontofrio",
         "tax": "18",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(ponto_result, 2)},
        {"service":"kabum",
         "tax": "14",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(kabum_result, 2)},
        {"service":"magazine",
         "tax": "20",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(magazine_result, 2)},
        {"service":"shopee",
         "tax": f"{round(shopee_result.tax, 0)}%",
         "shipping": shopee_result.shipping,
         "goverment_taxes": shopee_result.governement_taxes,
         "amount": round(shopee_result.selling_price, 2)},
        {"service":"aliexpress",
         "tax": "10",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(aliexpress_result, 2)},
        {"service":"submarino",
         "tax": f"{round(submarino_result.tax, 0)}%",
         "shipping": submarino_result.shipping,
         "goverment_taxes": submarino_result.governement_taxes,
         "amount": round(submarino_result.selling_price, 2)},
        {"service":"olist",
         "tax": "21",
         "shipping": "17",
         "goverment_taxes": goverment_taxes,
         "amount": round(olist_result, 2)}
    ]

    #json.dumps(prices_result)

    return jsonify(prices_result)   