import json
import requests
from app import app
from app.models import product

def getProductInfo(sku):    
    # importing the requests library

    # api-endpoint
    URL = "https://bling.com.br/Api/v2/produtos/json/&apikey=6d50db97e7f87778cf4d98d162a9aaa9d9536da2853a8fb80f43f3483ace493f6389554d"

    # sending get request and saving the response as response object
    response = requests.get(url = URL)

    # extracting data in json format
    result = json.loads(response.text)
    
    produtos = result['retorno']['produtos']

    for produto in produtos:
        id = produto['produto']['id']
        cod = produto['produto']['codigo']
        name = produto['produto']['descricao']
        price = produto['produto']['preco']
        productImage = produto['produto']['imageThumbnail']
        marca = produto['produto']['marca']
        pesoLiq = produto['produto']['pesoLiq']
        pesoBruto = produto['produto']['pesoBruto']
        gtin = produto['produto']['gtin']
        gtinEmbalagem = produto['produto']['gtinEmbalagem']
        larguraProduto = produto['produto']['larguraProduto']
        alturaProduto = produto['produto']['alturaProduto']
        profundidadeProduto = produto['produto']['profundidadeProduto']


        if cod == sku:
            return product(id, cod, name, price, productImage, marca, pesoLiq, pesoBruto, gtin, gtinEmbalagem, larguraProduto, alturaProduto, profundidadeProduto)