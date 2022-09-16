from app import app

def getProductInfoBySku(sku):    
    #Pegar com o SKU os dados do produto no bling
    #Pegar a categoria do produto no ML (https://developers.mercadolivre.com.br/pt_br/categorizacao-de-produtos) "https://api.mercadolibre.com/sites/$SITE_ID/domain_discovery/search?q=$NOME_PRODUTO"
    #Com o category ID buscar o preço (https://developers.mercadolivre.com.br/pt_br/comissao-por-vender) "https://api.mercadolibre.com/sites/$SITE_ID/listing_prices?price=500&category_id=MLB1055"
    pass