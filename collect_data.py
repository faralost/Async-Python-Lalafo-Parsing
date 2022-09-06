import time
from datetime import datetime

from parse_lalafo import get_json_for_rental_estate_items_by_category, get_json_for_item_details

CATEGORY_IDS = [2046, 2031, 2038, 2055, 5301, 2044, 2045, 2033, 2034, 2039, 2064, 5299, ]


def collecting_result_data(category_id, per_page):
    start = time.time()
    response_data = get_json_for_rental_estate_items_by_category(category_id=category_id, per_page=per_page)
    end = time.time()
    print(f'finished request for category_id={category_id} in {end - start} seconds...')
    print(f'ok got {len(response_data["items"])} items from lalafo category_id={category_id}')

    result = []
    for item in response_data['items']:

        images = []
        for image in item['images']:
            images.append(image['original_url'])

        detail_start = time.time()
        detail = get_json_for_item_details(item_id=item['id'])
        detail_end = time.time()
        print(f'finished detail request for item_id={item["id"]} in {detail_end - detail_start} seconds...')

        square = None
        add_from = None
        for param in detail['params']:
            if param['id'] == 70:
                square = param['value']
            if param['id'] == 952:
                add_from = param['value']

        result.append({
            'created_time': datetime.fromtimestamp(item['created_time']).strftime('%d-%m-%Y %H:%M:%S'),
            'city': item['city_alias'],
            'currency': item['currency'],
            'price': item['price'],
            'images_url': images,
            'phone_number': item['mobile'],
            'title': item['title'],
            'description': item['description'],
            'square': float(square),
            'add_from': add_from,  # риэлтор или хозяин
        })

    return result


print(collecting_result_data(category_id=2031, per_page=5))
