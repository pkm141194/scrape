from time import sleep
from datetime import datetime
from requests import get, post
from string import punctuation
from selenium import webdriver
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

get_url = "https://tcesffb3s8.execute-api.ap-south-1.amazonaws.com/dev/productscraping/getinput"
post_url = "https://tcesffb3s8.execute-api.ap-south-1.amazonaws.com/dev/sitestatsTEST"

def get_data():
    
    # For API
    # while True:
    #     data_dict = get(get_url).json()
    #     if data_dict['responseCode'] == 200:
    #         break
    #     else:
    #         print('Data not available..')
    #         sleep(4)
    # For testing
    data_dict = {
        "responseCode": 200,
        "responseMessage": "get scraping data from rabbitmq successfully",
        "preferencePojo": {
            "preferenceId": 84,
            "userId": 1,
            "url_scrap": "https://www.harveynorman.com.au/ ",
            "product_scrap": 'Samsung Galaxy S10+ 128GB - Prism Green',
            "createdDate": "2021-02-25 05:34:10",
            "category": "Mobile",
            "sku": "sku",
            "price": 5,
            "variancepercentage": 0,
            "status": 0,
            "seller": "Xtreme"
        }
    }
    
    if data_dict['responseCode'] != 200:
        return False, False, False, False
    prd = data_dict['preferencePojo']
    name = prd['product_scrap']
    price = prd['price']
    seller = prd['seller']
    print(seller)
    return True, name, price, seller, prd




