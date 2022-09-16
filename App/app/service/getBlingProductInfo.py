import requests
from app import app
from app.models import product

def getBlingProductInfo(sku):    
    # importing the requests library

    # api-endpoint
    URL = "https://bling.com.br/Api/v2/produtos/json/&apikey=6d50db97e7f87778cf4d98d162a9aaa9d9536da2853a8fb80f43f3483ace493f6389554d"

    # sending get request and saving the response as response object
    r = requests.get(url = URL)

    # extracting data in json format
    data = r.json()
    
    produtos = data['retorno']['produtos']
    for produto in produtos:
        produto = produto['produto']
        if produto['codigo'] == sku:
            product(produto['id'], 
                    produto['codigo'], 
                    produto['descricao'], 
                    produto['preco'], 
                    produto['imageThumbnail'],
                    produto['marca'], 
                    produto['pesoLiq'], 
                    produto['pesoBruto'], 
                    produto['gtin'], 
                    produto['gtinEmbalagem'], 
                    produto['larguraProduto'], 
                    produto['alturaProduto'], 
                    produto['profundidadeProduto']
                )
        

    return product