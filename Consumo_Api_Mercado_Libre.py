import requests
import json
import logging


items = 'https://api.mercadolibre.com/sites/MLA/search?seller_id=179571326&attributes=results'
categories = 'https://api.mercadolibre.com/sites/MLA/search?seller_id=179571326&category='


organized_items = []

logging.basicConfig(filename="Logs_Items.log", level=logging.INFO)



def get_items_api():
    response = requests.get(items)

    if response.status_code == 200 :
        Items_response = response.json()

    return Items_response


def get_categories_api(id_categories):

    response = requests.get(categories+str(id_categories))

    if response.status_code == 200 :
        categories_response= response.json()

    return categories_response['filters'][0]['values'][0]['name']
   
  


def organize_data(Items):

    for item in range(len(Items['results'])):
        organized_items.append(
            {
            "id_item_"+str(item+1):Items['results'][item]['id'],
            "title_del_item":Items['results'][item]['title'],
            "categoria_id":Items['results'][item]['category_id'],
            "name_categoria":get_categories_api(Items['results'][item]['category_id'])
            }
            )

        logging.info(organized_items[item])
    


if __name__ == '__main__':
    organize_data(get_items_api())


